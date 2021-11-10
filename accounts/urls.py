from django.urls import path
from .views import log,reg
from django.contrib.auth import views

urlpatterns = [
    path('',reg, name = 'register'),
    path('login/', views.LoginView.as_view(template_name = 'accounts/log.html'), name = 'login')
]
