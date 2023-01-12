from django.urls import path
from django.contrib.auth import views as auth_views

from accounts import views
from accounts.views import CustomPasswordResetView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        redirect_authenticated_user=True),
        name="login"),
    path('register/', views.register_view, name="register"),
    path('lougout/', views.logout_view, name="logout"),
    path('profile/', views.profile_view, name="profile"),

    # Reset password
    path('reset_password/', CustomPasswordResetView.as_view(
        template_name="account/password_reset.html"),
        name="password_reset"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name="account/password_reset_done.html"),
        name="password_reset_done"),
    path('reset_password_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="account/password_reset_confirm.html"),
        name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="account/password_reset_complete.html"),
        name="password_reset_complete"),

    # Change password
    path('password/', auth_views.PasswordChangeView.as_view(
        template_name="account/password_change.html"),
        name="password_change"),
    path('password/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name="account/password_change_done.html"),
        name="password_change_done")
]
