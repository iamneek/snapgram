from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed_view, name='feed'),
    path('like/<int:post_id>/', views.toggle_like, name='like'),
]