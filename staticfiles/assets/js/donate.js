// Quick amount buttons
document.querySelectorAll('.quick-amount').forEach(btn => {
  btn.addEventListener('click', () => {
    document.getElementById('amount').value = btn.dataset.value;
  });
});

// Form submission placeholder
document.getElementById('donationForm').addEventListener('submit', (e) => {
  e.preventDefault();

  const amount = document.getElementById('amount').value;
  const email = document.getElementById('donorEmail').value;

  if (!amount || amount <= 0) {
    alert('Please enter a valid donation amount.');
    return;
  }

  alert(`Thank you for donating ₦${amount}! We’ll process your payment (demo only).`);

  // Later: integrate Paystack here
});
