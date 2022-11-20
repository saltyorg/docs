# Container Healthchecks

Saltbox can set a custom healthcheck on a Docker container via the inventory system.

The syntax for this

```yaml
<rolename>_docker_healthcheck:
  test: ["healthcheck", "in", "command", "notation"]
  interval: 10s
  timeout: 5s
  retries: 10
  start_period: 10s
```

Below are some samples for various available roles:

```yaml
postgres_docker_healthcheck:
  test: ["CMD-SHELL", "pg_isready", "-d", "{{ postgres_docker_env_db }}"]
  interval: 10s
  timeout: 5s
  retries: 10
  start_period: 10s

aria2_ng_docker_healthcheck:
  test: ["CMD", "curl", "--fail", "http://localhost:8080"]
  interval: 10s
  timeout: 5s
  retries: 10
  start_period: 10s

docspell_docker_healthcheck:
  test: ["CMD", "wget", "--spider", "http://localhost:{{ docspell_web_port }}/api/info/version"]
  interval: 1m
  timeout: 10s
  retries: 2
  start_period: 30s

duplicati_docker_healthcheck:
  test: ["CMD", "curl", "--fail", "http://localhost:{{ duplicati_web_port }}"]
  interval: 10s
  timeout: 5s
  retries: 10
  start_period: 10s

elasticsearch_docker_healthcheck:
  test: ["CMD", "curl", "--fail", "http://localhost:9200"]
  interval: 10s
  timeout: 5s
  retries: 10
  start_period: 10s

gaps_docker_healthcheck:
  test: ["CMD", "curl", "--fail", "http://localhost:8484"]
  interval: 10s
  timeout: 5s
  retries: 10
  start_period: 10s

heimdall_docker_healthcheck:
  test: ["CMD", "curl", "--fail", "http://localhost:80"]
  interval: 10s
  timeout: 5s
  retries: 10
  start_period: 10s

homeassistant_docker_healthcheck:
  test: ["CMD", "curl", "--fail", "http://localhost:{{ homeassistant_web_port }}"]
  interval: 10s
  timeout: 5s
  retries: 10
  start_period: 10s

koel_docker_healthcheck:
  test: ["CMD", "curl", "--fail", "http://localhost"]
  interval: 10s
  timeout: 5s
  retries: 10
  start_period: 10s

lunasea_docker_healthcheck:
  test: ["CMD", "curl", "--fail", "http://localhost"]
  interval: 10s
  timeout: 5s
  retries: 10
  start_period: 10s

omegabrr_docker_healthcheck:
  test: ["CMD", "curl", "--fail", "http://localhost:{{ omegabrr_web_port }}/api/webhook/trigger"]
  interval: 10s
  timeout: 5s
  retries: 10
  start_period: 10s

phpmyadmin_docker_healthcheck:
  test: ["CMD", "curl", "--fail", "http://localhost:{{ phpmyadmin_web_port }}"]
  interval: 10s
  timeout: 5s
  retries: 10
  start_period: 10s

plexshare_docker_healthcheck:
  test: ["CMD", "curl", "--fail", "http://localhost:{{ plexshare_web_port }}"]
  interval: 10s
  timeout: 5s
  retries: 10
  start_period: 10s

reposilite_docker_healthcheck:
  test: ["CMD", "curl", "--fail", "http://localhost:{{ reposilite_web_port }}"]
  interval: 10s
  timeout: 5s
  retries: 10
  start_period: 10s

rflood_docker_healthcheck:
  test: ["CMD", "curl", "--fail", "http://localhost:3000"]
  interval: 10s
  timeout: 5s
  retries: 10
  start_period: 10s

solr_docker_healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:{{ solr_docker_env_port }}/solr/{{ solr_docker_env_core_name }}/admin/ping"]
  interval: 1m
  timeout: 10s
  retries: 5
  start_period: 30s

tubearchivist_docker_healthcheck:
  test: ["CMD", "curl", "--fail", "http://localhost:{{ tubearchivist_web_port }}"]
  interval: 10s
  timeout: 5s
  retries: 10
  start_period: 10s

tvheadend_docker_healthcheck:
  test: ["CMD", "curl", "--fail", "http://localhost:{{ tvheadend_web_port }}"]
  interval: 10s
  timeout: 5s
  retries: 10
  start_period: 10s

wikijs_docker_healthcheck:
  test: ["CMD", "curl", "--fail", "http://localhost:3000"]
  interval: 10s
  timeout: 5s
  retries: 10
  start_period: 10s
```
