from django.conf.urls import url, include
from accounts.views import logout, login
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='../templates/password/reset_password.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='../templates/password/password_reset_done.html'), name='password_reset_done'),
    path('reset<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    ]