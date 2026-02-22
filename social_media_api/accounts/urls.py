from django.urls import path
from django.http import HttpResponse

from .views import FollowUserView, UnfollowUserView

def test_view(request):
    return HttpResponse("Accounts working!")

urlpatterns = [
    path('', test_view),
]

from .views import RegisterView, LoginView, ProfileView

urlpatterns += [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),

    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
   
]