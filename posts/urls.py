from django.urls import path
from . import views

urlpatterns = [
     path('groups/<int:pk>/posts/create/', views.PostCreate.as_view()),
     path('groups/<int:pk>/posts/', views.PostList.as_view()),
]
