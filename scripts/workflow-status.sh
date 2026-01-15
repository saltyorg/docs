#!/bin/bash

# Pass GitHub token, repository, and run ID as arguments
GITHUB_TOKEN=$1
GITHUB_REPOSITORY=$2
GITHUB_RUN_ID=$3

if [ -z "$GITHUB_TOKEN" ] || [ -z "$GITHUB_REPOSITORY" ] || [ -z "$GITHUB_RUN_ID" ]; then
  echo "Usage: $0 <github_token> <github_repository> <github_run_id>"
  exit 1
fi

max_attempts=5
page=1
declare -A conclusion_counts

# Initialize conclusions to avoid integer expression expected error
for status in success failure cancelled skipped neutral timed_out action_required unknown; do
  conclusion_counts[$status]=0
done

log() {
  echo "[workflow-status] $*"
}

log "Starting workflow status check for run $GITHUB_RUN_ID in $GITHUB_REPOSITORY"

while :; do
  success=false
  for attempt in $(seq 1 $max_attempts); do
    log "Attempt $attempt of $max_attempts for page $page"

    url="https://api.github.com/repos/$GITHUB_REPOSITORY/actions/runs/$GITHUB_RUN_ID/jobs?page=$page&per_page=100"
    log "Requesting $url"

    response_with_headers=$(curl -sS -D - -H "Authorization: token $GITHUB_TOKEN" \
      -H "Accept: application/vnd.github+json" "$url")
    curl_exit=$?

    if [ $curl_exit -ne 0 ]; then
      log "curl failed with exit code $curl_exit, retrying in $((attempt * 2)) seconds..."
      sleep $((attempt * 2))
      continue
    fi

    normalized=$(printf '%s' "$response_with_headers" | tr -d '\r')
    if [[ "$normalized" == *$'\n\n'* ]]; then
      header=${normalized%%$'\n\n'*}
      body=${normalized#*$'\n\n'}
    else
      header="$normalized"
      body=""
    fi

    http_status=$(printf '%s\n' "$header" | awk 'toupper($1) ~ /^HTTP/ {code=$2} END {print code}')
    link_header=$(printf '%s\n' "$header" | awk -F': ' 'tolower($1)=="link"{print $2}' | tail -n1)
    rate_remaining=$(printf '%s\n' "$header" | awk -F': ' 'tolower($1)=="x-ratelimit-remaining"{print $2}' | tail -n1)
    rate_reset=$(printf '%s\n' "$header" | awk -F': ' 'tolower($1)=="x-ratelimit-reset"{print $2}' | tail -n1)

    rate_reset_human=""
    if [ -n "$rate_reset" ]; then
      rate_reset_human=$(date -u -d "@$rate_reset" +%H:%M:%SZ 2>/dev/null || true)
    fi

    rate_msg="rate remaining: ${rate_remaining:-unknown}"
    if [ -n "$rate_reset_human" ]; then
      rate_msg="$rate_msg, reset: $rate_reset_human"
    fi

    log "HTTP status: ${http_status:-unknown}, $rate_msg"

    if [ "$http_status" != "200" ]; then
      api_message=$(echo "$body" | jq -r '.message // empty' 2>/dev/null)
      if [ -n "$api_message" ]; then
        log "API error message: $api_message"
      elif [ -n "$body" ]; then
        log "API response body: $(echo "$body" | head -c 200)"
      fi
      log "Non-200 response, retrying in $((attempt * 2)) seconds..."
      sleep $((attempt * 2))
      continue
    fi

    if ! echo "$body" | jq -e . >/dev/null 2>&1; then
      log "Invalid JSON response, retrying in $((attempt * 2)) seconds..."
      sleep $((attempt * 2))
      continue
    fi

    job_conclusions=$(echo "$body" | jq -r '.jobs[].conclusion' 2>/dev/null)
    jq_exit=$?
    if [ $jq_exit -ne 0 ]; then
      log "Failed to parse job conclusions (jq exit $jq_exit), retrying in $((attempt * 2)) seconds..."
      sleep $((attempt * 2))
      continue
    fi

    jobs_total=$(echo "$body" | jq -r '.total_count // 0' 2>/dev/null)
    job_count=$(printf '%s' "$job_conclusions" | awk 'END {print NR}')
    log "Parsed $job_count jobs from page $page (API total_count: $jobs_total)."

    if [ -z "$job_conclusions" ]; then
      log "No job conclusions returned for page $page."
    fi

    while IFS= read -r line; do
      # Handle null or unexpected values
      if [[ -z "$line" || "$line" == "null" ]]; then
        ((conclusion_counts[unknown]++))
      elif [[ -n "${conclusion_counts[$line]+x}" ]]; then
        ((conclusion_counts[$line]++))
      else
        ((conclusion_counts[unknown]++))
        log "Unexpected conclusion value '$line' (counted as unknown)."
      fi
    done <<< "$job_conclusions"

    log "Counts so far: success=${conclusion_counts[success]} failure=${conclusion_counts[failure]} cancelled=${conclusion_counts[cancelled]} skipped=${conclusion_counts[skipped]} neutral=${conclusion_counts[neutral]} timed_out=${conclusion_counts[timed_out]} action_required=${conclusion_counts[action_required]} unknown=${conclusion_counts[unknown]}"

    success=true
    break
  done

  if [ "$success" = false ]; then
    log "API requests failed after $max_attempts attempts, defaulting to failure."
    exit 1
  fi

  # Check for next page using the Link header
  if echo "$link_header" | grep -q 'rel="next"'; then
    page=$((page + 1))
    log "Pagination detected, moving to page $page."
  else
    log "No more pages detected."
    break
  fi
done

# Determine overall workflow conclusion
if [ ${conclusion_counts[failure]} -gt 0 ] || [ ${conclusion_counts[timed_out]} -gt 0 ] || [ ${conclusion_counts[action_required]} -gt 0 ]; then
  WORKFLOW_CONCLUSION="failure"
elif [ ${conclusion_counts[cancelled]} -gt 0 ]; then
  WORKFLOW_CONCLUSION="cancelled"
elif [ ${conclusion_counts[success]} -gt 0 ] || [ ${conclusion_counts[skipped]} -gt 0 ] || [ ${conclusion_counts[neutral]} -gt 0 ]; then
  WORKFLOW_CONCLUSION="success"
else
  WORKFLOW_CONCLUSION="failure"
fi

# Export WORKFLOW_CONCLUSION to GitHub Actions environment
log "Final workflow conclusion: $WORKFLOW_CONCLUSION"
echo "WORKFLOW_CONCLUSION=$WORKFLOW_CONCLUSION" >> "$GITHUB_ENV"
