from django.urls import path
from . import views

urlpatterns = [
    path("", views.feed_view, name="feed"),
    path("like/<int:post_id>/", views.toggle_like, name="like"),
    path("posts/<int:post_id>/", views.post_detail_view, name="post_detail"),
    path(
        "comment/create/<int:post_id>/",
        views.create_comment_view,
        name="create_comment",
    ),
    path(
        "comment/delete/<int:comment_id>/",
        views.delete_comment_view,
        name="delete_comment",
    ),
]
