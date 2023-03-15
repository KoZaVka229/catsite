from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='my_profile'),
    path('profile/<int:user_id>/', views.ProfileView.as_view(), name='user_profile'),
    path('profile/create/', views.CreateProfile.as_view(), name='create_profile'),
    path('profile/edit/', views.EditProfile.as_view(), name='edit_profile'),

    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.SignInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
