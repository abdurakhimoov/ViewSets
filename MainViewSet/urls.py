from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieViewSet.as_view())
]