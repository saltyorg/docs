document$.subscribe(function () {

  /* Role Defaults override-level visibility toggle */
  updateToggleDisplay();

  document.addEventListener('click', function (event) {
    if (event.target && event.target.id === 'sb-checkbox--var-level') {
      updateToggleDisplay();
    }
  });

  function updateToggleDisplay() {
    const toggleCheckbox = document.getElementById('sb-checkbox--var-level');
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
});