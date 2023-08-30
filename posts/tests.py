from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post
from groups.models import Group, GroupMembership


class PostCreateTests(APITestCase):
    """
    Tests for the Posts model create view
    """
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.group = Group.objects.create(
            name='Test Group', description='Test group description',
            created_by=self.user
        )
        self.member_user = User.objects.create_user(
            username='member', password='testpassword'
        )
        self.membership = GroupMembership.objects.create(
            user=self.member_user, group=self.group
        )
        self.post_data = {
            'title': 'Test Post',
            'content': 'Test content',
        }

    def test_user_not_logged_in_cant_create_post(self):
        response = self.client.post(
            reverse('post-create', kwargs={'pk': self.group.id}),
            self.post_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Post.objects.count(), 0)

    def test_user_not_member_cant_create_post(self):
        user2 = User.objects.create_user(
            username='testuser2', password='testpassword'
        )
        self.client.login(username='testuser2', password='testpassword')
        response = self.client.post(
            reverse('post-create', kwargs={'pk': self.group.id}),
            self.post_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Post.objects.count(), 0)

    def test_create_post_as_member(self):
        self.client.login(username='member', password='testpassword')
        response = self.client.post(
            reverse('post-create', kwargs={'pk': self.group.id}),
            self.post_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_post_as_creator(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('post-create', kwargs={'pk': self.group.id}),
            self.post_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
