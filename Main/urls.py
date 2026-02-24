from django.urls import path
from . import views 


urlpatterns = [
	path("", views.index, name="index"),
	path("register/", views.register_member, name="register"),
	path("login/", views.login_view, name="login")
]

