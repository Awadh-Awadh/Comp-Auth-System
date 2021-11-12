from django.urls import path
from .views import log,reg,landing_page, home
from django.contrib.auth import views

urlpatterns = [
    path('register/',reg, name = 'register'),
    path('login/', views.LoginView.as_view(template_name = 'account/login.html'), name = 'login'),
    path('', landing_page, name = "landing"),
    path('home/' ,home, name = "home"),
    path('logout/', views.LogoutView.as_view(), name = "logout"),
]
