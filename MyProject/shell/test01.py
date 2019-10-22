from django.contrib.auth.models import User

from boards.models import Board, Topic, Post

user = User.objects.first()

for i in range(100):
    subject = 'Topic test #{}'.format(i)
    topic = Topic.objects.create(subject=subject, board=Board.objects.get(name='Django'), starter=user)
    Post.objects.create(message='Lorem issum...', topic=topic, created_by=user)