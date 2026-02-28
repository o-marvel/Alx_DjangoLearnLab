from django.urls import path
from django.http import HttpResponse

# from .views import  follow_user,unfollow_user,list_users

def test_view(request):
    return HttpResponse("Accounts working!")

urlpatterns = [
    path('', test_view),
]

from .views import RegisterView, LoginView, ProfileView

from . import views
urlpatterns += [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
   
    path('follow/<int:user_id>/', views.follow_user),
    path('unfollow/<int:user_id>/', views.unfollow_user),
    # path('follow/<int:user_id>/', follow_user, name='follow-user'),
    # path('unfollow/<int:user_id>/', unfollow_user, name='unfollow-user'),
    # path('users/', list_users, name='list-users'),
   
]