from django.urls import path
from .views import custom_logout,signup_view, CustomPasswordResetView, login_view
from . import views

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    # Add other password reset related URLs here...
]
