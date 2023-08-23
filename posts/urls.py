from django.urls import path
from . import views

urlpatterns = [
     path(
          'groups/<int:pk>/posts/create/', views.PostCreate.as_view(),
          name='post-create'),
     path('groups/<int:pk>/posts/', views.PostList.as_view()),
     path('groups/<int:group_pk>/posts/<int:pk>', views.PostDetail.as_view()),
]
