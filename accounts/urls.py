from django.urls import path
from .views import log,reg,landing_page, home, verify_view
from django.contrib.auth import views

urlpatterns = [
    path('register/',reg, name = 'register'),
    path('login/', log, name = 'login'),
    path('', landing_page, name = "landing"),
    path('home/' ,home, name = "home"),
    path('logout/', views.LogoutView.as_view(), name = "logout"),
    path('verify/', verify_view, name = 'verify' )
]
