from django.urls import path
from . import views 


urlpatterns = [
	path("", views.index, name="index"),
	path("register/", views.register_member, name="register"),
	path("login/", views.login_view, name="login"),
	path("logout/", views.logout_view, name="logout"),
	path("dashboard/", views.dashboard, name="dashboard"),
	path("about/", views.about, name='about'),
	path("bog/", views.bog, name='bog')
]

