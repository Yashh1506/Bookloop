from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name = 'login'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('edit_profile/', views.edit_profile, name='edit-profile'),
    path('<int:user_id>', views.users, name='users'),
    path('chat/<str:username>', views.chat_view, name='chat'),
    path('user_profile/<str:username>', views.user_profile, name='user_profile')
]