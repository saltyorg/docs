document$.subscribe(function () {

// Role Defaults override-level visibility toggle
  updateToggleDisplay();

  document.addEventListener('click', function (event) {
    if (event.target && event.target.matches('.sb-toggle--override-scope input[type="checkbox"]')) {
      updateToggleDisplay();
    }
  });

  function updateToggleDisplay() {
    const toggleCheckbox = document.querySelector('.sb-toggle--override-scope input[type="checkbox"]');
    if (!toggleCheckbox) return;

    const isChecked = toggleCheckbox.checked;

    document.querySelectorAll('.sb-show-on-unchecked').forEach(el => {
      el.style.display = isChecked ? 'none' : 'block';
    });
    document.querySelectorAll('.sb-show-on-checked').forEach(el => {
      el.style.display = isChecked ? 'block' : 'none';
    });
  }

// Content tabs - custom background colors
  function setActiveTabColor() {
    document.querySelectorAll('.md-typeset .tabbed-set').forEach(tabSet => {
      const inputs = tabSet.querySelectorAll('input[type="radio"]');
      const labels = tabSet.querySelectorAll('.tabbed-labels > label');
      inputs.forEach((input, idx) => {
        if (labels[idx]) {
          if (input.checked) {
            labels[idx].style.backgroundColor = 'color-mix(in srgb, var(--md-primary-fg-color), transparent 70%)';
          } else {
            labels[idx].style.backgroundColor = '';
          }
        }
      });
    });
  }

  setActiveTabColor();

  document.addEventListener('change', function (event) {
    if (event.target.matches('.md-typeset .tabbed-set > input[type="radio"]')) {
      setActiveTabColor();
    }
  });

// Open same-origin link to non-markdown page in a new tab
  document.querySelectorAll('a[href]').forEach(function (link) {
    const href = link.getAttribute('href');
    if (href && !href.startsWith('#')) {
      const url = new URL(href, window.location.origin);
      if (url.origin === window.location.origin && /\.[^/]+$/.test(url.pathname)) {
        link.setAttribute('target', '_blank');
      }
    }
  });
});