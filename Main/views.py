from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User 
from django.contrib import messages 
from .models import Member
from django.contrib.auth import authenticate, login, logout

from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re

from django.contrib.auth.decorators import login_required

# Create your views here.



def index(request):
	return render(request, 'index.html')


def register_member(request):
    if request.method == "POST":
        # Get data safely
        full_name = request.POST.get("fullName", "").strip()
        email = request.POST.get("email", "").strip().lower()
        password = request.POST.get("password", "")
        phone = request.POST.get("phone", "").strip()
        address = request.POST.get("address", "").strip()
        role = request.POST.get("role", "")
        photo = request.FILES.get("photo")
        consent = request.POST.get("consent")

        errors = []

        # 1. Validate Inputs
        if not full_name:
            errors.append("Full name is required")
        
        if not email:
            errors.append("Email is required")
        else:
            try:
                validate_email(email)
            except ValidationError:
                errors.append("Invalid email format")

        if len(password) < 7:
            errors.append("Password must be at least 7 characters")

        # Nigerian Phone Validation
        phone_pattern = r'^(?:\+234|0)[7-9][0-1]\d{8}$'
        if not re.match(phone_pattern, phone):
            errors.append("Enter a valid Nigerian phone number (e.g., +2348012345678)")

        if not role:
            errors.append("Please select a role")

        if not consent:
            errors.append("You must agree to Terms & Conditions")

        # 2. Check Existing User
        if User.objects.filter(username=email).exists():
            errors.append("Email already registered")

        # 3. Handle Errors
        if errors:
            for error in errors:
                messages.error(request, error)
            return render(request, "join.html")

        # 4. Create User & Profile
        try:
            user = User.objects.create_user(username=email, email=email, password=password)
            
            member = Member.objects.create(
                user=user,
                email=email,
                full_name=full_name,
                mobile_no=phone,
                address=address,
                role=role,
                photo=photo
            )
            
            messages.success(request, "Registration successful! Please log in.")
            login(request, user)
            return redirect("dashboard")
            
        except Exception as e:
            messages.error(request, f"Registration failed: {str(e)}")
            return render(request, "join.html")

    return render(request, "join.html")


"""
def register_member(request):
	if request.method == "POST":
		full_name = request.POST.get("fullName")
		email = request.POST.get("email")
		password = request.POST.get("password")
		phone = request.POST.get("phone")
		address = request.POST.get("address")
		role = request.POST.get("role")
		photo = request.FILES.get("photo")

		# check if user already exists 

		if User.objects.filter(username=email).exists():
			return render(request, "join.html", {"error": "Email already registered"})


		# create user 
		user = User.objects.create_user(username=email, email=email, password=password)

		# create member profile 
		member = Member.objects.create(user=user, email=email, full_name=full_name, mobile_no=phone, address=address, role=role, photo=photo)

		return redirect("login")
	return render(request, "join.html")
"""

def login_view(request):
	if request.method == "POST":
		email = request.POST.get("email")
		password = request.POST.get("password")

		user = authenticate(request, username=email, password=password)

		if user is not None:
			login(request, user)

			return redirect("index")
		else:
			return render(request, "login.html", {"error": "Invalid login credentials"})
	return render(request, "login.html")



@login_required
def dashboard(request):
    # Safer than .get() - returns 404 if member doesn't exist
    member = get_object_or_404(Member, user=request.user)
    return render(request, "dashboard.html", {"member": member})




def logout_view(request):
    """
    Log out the user and redirect to homepage with success message.
    """
    if request.method == "POST":  # Best practice: logout via POST to prevent CSRF attacks
        logout(request)
        messages.success(request, "You have been successfully logged out. See you soon! 👋")
        return redirect("index")  # Replace with your actual home URL name
    return redirect("index")  # Fallback redirect if accessed via GET

"""
@login_required
def dashboard(request):
    member = Member.objects.get(user=request.user)

    return render(request, "dashboard.html", {"member": member})
"""
def about(request):
    return render(request, "about.html")

def bog(request):
    return render(request, "bog.html")
