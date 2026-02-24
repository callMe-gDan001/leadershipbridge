import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Fixed: Use list of tuples with (value, display_name)
# These values MUST match what your HTML form sends
ROLE_CHOICES = [
    ('Volunteer', 'Volunteer'),
    ('Community Leader', 'Community Leader'),
    ('Donor', 'Donor'),
    ('Trainee', 'Trainee'),
]

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership_id = models.CharField(max_length=20, unique=True, blank=True)
    full_name = models.CharField(max_length=150)
    email = models.EmailField()  # Removed default - should come from form
    photo = models.ImageField(upload_to='member_photos/', blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True)
    # Made optional since it's not in your HTML form
    id_card = models.FileField(upload_to='id_cards/', blank=True, null=True)
    mobile_no = models.CharField(max_length=15)
    address = models.TextField()
    # Fixed: max_length matches longest choice value
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        # Generate membership_id only if it doesn't exist
        if not self.membership_id:
            self.membership_id = str(uuid.uuid4())[:8].upper()
        # Call super().save() ONCE outside the if block
        super().save(*args, **kwargs)