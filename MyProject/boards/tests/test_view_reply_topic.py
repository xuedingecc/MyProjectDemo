from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from boards.models import Board, Topic, Post


class ReplyTopicTestCase(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django boards.')
        self.username = 'john'
        self.password = '123'
        user = User.objects.create_user(username='john', email='john@doe.com', password='123')
        self.topic = Topic.objects.create(subject='Hello, world.', board=self.board, starter=user)
        Post.objects.create(message='Learn more', topic=self.topic, created_by=user)
        self.url = reverse('reply_topic', kwargs={'pk': self.board.pk, 'topic_pk': self.topic.pk})


class LoginRequireReplyTopicTests(ReplyTopicTestCase):
    pass


class ReplyTopicTests(ReplyTopicTestCase):
    pass


class SuccessfulReplyTopicTests(ReplyTopicTestCase):
    def test_redirection(self):
        url = reverse('topic_posts', kwargs={'pk': self.board.pk, 'topic_pk': self.topic.pk})
        topic_posts_url = '{url}?page=1#2'.format(url=url)
        self.assertRedirects(self.response, topic_posts_url)


class InvalidReplyTopicTests(ReplyTopicTestCase):
    pass
