from django.contrib.auth.models import User

from boards.models import Topic, Post

user = User.objects.first()

for i in range(22):
    message = 'Test #{}'.format(i)
    Post.objects.create(message=message, topic=Topic.objects.get(subject='Hi'), created_by=user)
