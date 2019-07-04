from django.contrib.auth import views
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='users-login'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('forgetpassword/', views.PasswordResetView.as_view(), name='users-forgetpassword'),
    path('admin/panel/', AdminView.as_view(), name='users-panel'),

]
