from django.urls import path
from . import views
app_name = 'users'
urlpatterns = [
    # safety_report views
#    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('profile/edit_profile/<str:username>', views.edit_profile, name='edit-profile'),
    path('profile/edit_profile/<str:username>/submit', views.edit_profile_subit, name='edit-profile-submit'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('signup/check', views.signup_check, name='signup_check'),
]
