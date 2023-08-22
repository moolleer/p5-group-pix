from django.urls import path
from groups import views


urlpatterns = [
    path('groups/', views.GroupList.as_view()),
    path('groups/<int:pk>/', views.GroupDetail.as_view()),
    path('groupmemberships/', views.GroupMembershipList.as_view()),
    path('groups/<int:pk>/join/', views.GroupJoinView.as_view()),
    path('groups/<int:pk>/leave/', views.GroupMembershipLeave.as_view()),
]
