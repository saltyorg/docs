document$.subscribe(function() {
  updateToggleDisplay();

  document.addEventListener('click', function(event) {
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
});