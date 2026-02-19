from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet
from .views import FeedView
from . import views

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='user-feed'),
    path('<int:pk>/like/', views.like_post, name='like-post'),
    path('<int:pk>/unlike/', views.unlike_post, name='unlike-post'),
]
