from django.urls import path
from . import views

urlpatterns = [
    path(
        'groups/<int:pk>/discussions/',
        views.DiscussionListCreateView.as_view()),
    path(
        'groups/<int:group_pk>/discussions/<int:pk>/',
        views.DiscussionDetailView.as_view()),
    path(
        'groups/<int:group_pk>/discussions/<int:discussion_pk>/update-delete/',
        views.DiscussionDetailOwner.as_view()),
]
