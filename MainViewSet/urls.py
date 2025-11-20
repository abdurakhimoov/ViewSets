from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'movie', MovieViewSet, basename='movie')
router.register(r'comment', CommentViewSet, basename='comment')
urlpatterns = router.urls