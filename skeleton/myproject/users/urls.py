from django.urls import path
from .views import custom_login, custom_logout,signup_view, CustomPasswordResetView
from . import views

urlpatterns = [
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    # Add other password reset related URLs here...
]
