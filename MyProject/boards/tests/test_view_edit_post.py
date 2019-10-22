from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from boards.models import Board, Topic, Post


class PostUpdateViewTestCase(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board')
        self.username = 'john'
        self.password = '123'
        user = User.objects.create_user(username=self.username, email='john@doe.com', password=self.password)
        self.topic = Topic.objects.create(subject='hello word', board=self.board, starter=user)
        self.post = Post.objects.create(message='lorem ispum', topic=self.topic, created_by=user)
        self.url = reverse('edit_post', kwargs={
            'pk': self.board.pk,
            'topic_pk': self.topic.pk,
            'post_pk': self.post.pk
        })


class LoginRequiredPostUpdateViewTests(PostUpdateViewTestCase):
    def test_redirection(self):
        login_url = reverse('login')
        response = self.client.get(self.url)
        self.assertRedirects(response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))


class UnauthorizedPostUpdateViewTests(PostUpdateViewTestCase):
    def setUp(self):
        super().setUp()
        username = 'jane'
        password = '321'
        user = User.objects.create_user(username=username, email='jane@doe.com', password=password)
        self.client.login(username=username, password=password)
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 404)


class PostUpdateViewTests(PostUpdateViewTestCase):
    pass


class SuccessfulPostUpdateViewTests(PostUpdateViewTestCase):
    pass


class InvalidPostUpdateViewTests(PostUpdateViewTestCase):
    pass