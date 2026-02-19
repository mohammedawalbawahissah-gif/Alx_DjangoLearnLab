from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Post

User = get_user_model()

class LikeTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass1234')
        self.post_author = User.objects.create_user(username='author', password='pass1234')
        self.post = Post.objects.create(author=self.post_author, content='Hello world!')
        self.client.login(username='testuser', password='pass1234')

    def test_like_post(self):
        response = self.client.post(f'/posts/{self.post.id}/like/')
        self.assertEqual(response.status_code, 201)
