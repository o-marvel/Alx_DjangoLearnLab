from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [

     # Blog views
    path('post/', PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    # Auth views
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),
   
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


]
from .views import (
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView
)


urlpatterns += [
    path('post/<int:pk>/comments/new/',
         CommentCreateView.as_view(),
         name='comment_create'),

    path('comment/<int:pk>/update/',
         CommentUpdateView.as_view(),
         name='comment_update'),

    path('comment/<int:pk>/delete/',
         CommentDeleteView.as_view(),
         name='comment_delete'),
]
from .views import (
    PostsByTagView,
    SearchResultsView,
)

urlpatterns += [

    path(
        'tags/<slug:tag_slug>/',
        PostsByTagView.as_view(),
        name='posts_by_tag'
    ),

    path(
        'search/',
        SearchResultsView.as_view(),
        name='search_results'
    ),
]

