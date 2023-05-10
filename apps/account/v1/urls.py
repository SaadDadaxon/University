from django.urls import path, reverse, reverse_lazy
# from .views import login_views, register_views
from django.contrib.auth.views import LoginView,\
    PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView
from .views import RegisterView, logout_view, profile_info, profile_update, my_courses

urlpatterns = [
    # path('login/', login_views, name='login'),
    # path('register/', register_views, name='register'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name="login"),
    path('logout/', logout_view, name="logout"),
    path('register/', RegisterView.as_view(), name="register"),

    path('profile_info/', profile_info, name="profile_info"),
    path('update/<int:pk>', profile_update, name="profile_update"),
    path('my_courses/', my_courses, name="my_courses"),

    # Change password
    path('password_change/', PasswordChangeView.as_view(
        template_name='account/password_change/password_change.html', success_url=reverse_lazy('account:password_done')),
         name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='account/password_change/password_done.html'), name='password_done'),

    # Reset Password
    path('password_reset/send/', PasswordResetView.as_view(
        template_name='account/reset_password/password_reset_form.html',
        email_template_name='account/reset_password/password_reset_email.html',
        success_url=reverse_lazy('account:password_reset_done')),
         name='password_reset'),
    path('password_reset/done/',
         PasswordResetDoneView.as_view(template_name='account/reset_password/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset/confirm/<str:uidb64>/<str:token>/', PasswordResetConfirmView.as_view(
        template_name='account/reset_password/password_reset_confirm.html',
        success_url=reverse_lazy('account:password_reset_complete')),
         name='password_reset_confirm'),
    path('password_reset/complete/', PasswordResetCompleteView.as_view(
        template_name='account/reset_password/password_reset_complete.html'),
         name='password_reset_complete'),


]

