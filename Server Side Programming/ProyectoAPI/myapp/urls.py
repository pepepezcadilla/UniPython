# urls.py
from django.urls import path
from .views import UserListView, UserDetailView, PostListView, PostDetailView, CommentListView, CommentDetailView, AlbumListView, AlbumDetailView, PhotoListView, PhotoDetailView

app_name = 'myapp'
urlpatterns = [
    path('v1/users/', UserListView.as_view(), name='user-list'),
    path('v1/users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('v1/posts/', PostListView.as_view(), name='post-list'),
    path('v1/posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('v1/comments/', CommentListView.as_view(), name='comment-list'),
    path('v1/comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('v1/albums/', AlbumListView.as_view(), name='album-list'),
    path('v1/albums/<int:pk>/', AlbumDetailView.as_view(), name='album-detail'),
    path('v1/photos/', PhotoListView.as_view(), name='photo-list'),
    path('v1/photos/<int:pk>/', PhotoDetailView.as_view(), name='photo-detail'),
]
