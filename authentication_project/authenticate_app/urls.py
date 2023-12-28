from django.urls import path
from . import views

urlpatterns = [
    path('sign-in/', views.user_signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('change_password_by_old_password/', views.change_password_by_old_password, name='change_password_by_old_password'),
    path('change_password_without_old_password/', views.change_password_without_old_password, name='change_password_without_old_password'),
    path('update_user_data/', views.update_user_data, name='update_user_data'),
]
