from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Login and Logout
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Mainpage
    path('', views.mainpage, name='mainpage'),
    # Change Password
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # Reset Password
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_done'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    # Social Authentication
    path('social-auth/', include('social_django.urls', namespace='social'))
]

"""
we can use this path to hide all of this up path:
path('', include('django.contrib.auth.urls')) 
"""
