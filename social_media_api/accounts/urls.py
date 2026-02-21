from django.urls import path
from django.http import HttpResponse

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
]