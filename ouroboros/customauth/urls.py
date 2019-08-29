from django.contrib.auth import views as auth_views
from customauth import forms, views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="signup"),
    path(
        "login/",
        auth_views.LoginView.as_view(authentication_form=forms.LoginForm),
        name="login",
    ),
    path("resend_email/", views.ResendActivationEmailView.as_view(), name="resend_email"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path(
        "password_reset/",
        views.PlaceholderPasswordResetView.as_view(
            html_email_template_name="registration/password_reset_email.html",
            extra_email_context={"event_name": settings.EVENT_NAME},
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.PlaceholderPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("activate/<uidb64>/<token>/", views.ActivateView.as_view(), name="activate"),
]
