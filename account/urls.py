from django.urls import path
from . import views

app_name="account"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("forgot-password/", views.ForgotPasswordView.as_view(), name="forgot-password"),
    path("forgot-password/sent/", views.ForgotPasswordResetSentView.as_view(), name="reset-sent"),
    path("update-profile/", views.UpdateProfileView.as_view(), name="update-profile"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
]
