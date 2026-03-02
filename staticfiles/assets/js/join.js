document.getElementById('signupForm').addEventListener('submit', function(e) {
  e.preventDefault();

  // Basic front-end check for Nigerian phone pattern
  const phone = document.getElementById('phone').value.trim();
  const phonePattern = /^(?:\+234|0)[7-9][0-1]\d{8}$/;

  if (!phonePattern.test(phone)) {
    alert('Enter a valid Nigerian phone number');
    return;
  }

  alert('Form submitted successfully (front-end test)');
  // Later: send data to backend API
});
