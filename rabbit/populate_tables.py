
import datetime

from rabbit.models import Comment, Post, SubRabbit
from django.contrib.auth.models import User

hobbes = User.objects.get(username__exact='hobbes')

s1 = SubRabbit()
s1.name = 'rabbits'
s1.title = 'Rabbits'
s1.description = 'some description'
s1.sidebar = 'sidebar text'
s1.submission_text = 'submission text'
s1.datetime_created = datetime.datetime.now()
s1.owner = hobbes
s1.save()

s2 = SubRabbit()
s2.name = 'CaTs'
s2.title = 'Cats'
s2.description = 'The best animal'
s2.sidebar = "it's alright if you're a dog person as long as you like cats too"
s2.submission_text = 'submission text'
s2.datetime_created = datetime.datetime.now()
s2.owner = hobbes
s2.save()


p1 = Post()
p1.post_type = 'TEXT'
p1.title = 'post title'
p1.content = 'some post content'
p1.datetime_submitted = datetime.datetime.now()
p1.points = 1
p1.subrabbit = s1
p1.poster = hobbes
p1.save()

c1 = Comment()
c1.contents = 'comment contents'
c1.datetime_submitted = datetime.datetime.now()
c1.author = hobbes
c1.subrabbit = s1
c1.post = p1
c1.points = 1
c1.save()

c2 = Comment()
c2.contents = 'comment contents'
c2.datetime_submitted = datetime.datetime.now()
c2.author = hobbes
c2.subrabbit = s1
c2.post = p1
c2.points = 1
c2.save()



for i in range(20):
    p = Post()
    p.post_type = 'TEXT'
    p.title = f'post #{i}'
    p.content = 'some post content'
    p.datetime_submitted = datetime.datetime.now()
    p.points = 1
    p.subrabbit = s1
    p.poster = hobbes
    p.save()




from rabbit.models import Comment, Post, SubRabbit

for comment in Comment.objects.all():
    comment.delete()

for post in Post.objects.all():
    post.delete()

for sub in SubRabbit.objects.all():
    sub.delete()
