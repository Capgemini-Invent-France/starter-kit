from django.urls import path
from django.contrib.auth import views as auth_views

from . import views




urlpatterns = [
    path("register/",views.register,name= "register"),
    path("log_out/",views.log_out,name= "log_out"),
    path('reset_password/',auth_views.PasswordResetView.as_view(), name = "reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(), name = "password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name = "password_reset_confirm"),
    path('reset_password_completed/',auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]


