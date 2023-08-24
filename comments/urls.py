from django.urls import path
from . import views

urlpatterns = [
    path(
        'groups/<int:group_pk>/posts/<int:post_pk>/comments/',
        views.CommentList.as_view()),
    path(
        'groups/<int:group_pk>/posts/<int:post_pk>/comments/<int:pk>',
        views.CommentDetailPost.as_view()),
    path(
        'groups/<int:group_pk>/discussions/<int:discussion_pk>/comments/',
        views.CommentList.as_view()),
    path(
        'groups/<int:group_pk>/discussions/<int:discussion_pk>/comments/<int:pk>',
        views.CommentDetailDiscussion.as_view()),
]
