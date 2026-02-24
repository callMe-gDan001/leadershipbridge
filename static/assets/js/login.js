document.getElementById('loginForm').addEventListener('submit', function(e) {
  e.preventDefault();

  const email = document.getElementById('email').value.trim();
  const password = document.getElementById('password').value.trim();

  if (password.length < 8) {
    alert('Password must be at least 8 characters.');
    return;
  }

  // Placeholder for back-end integration
  alert(`Login attempt for: ${email}`);
});
