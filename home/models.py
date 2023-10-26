from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class blogPosts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    images = models.ImageField(blank=False, null=False, upload_to='images/%y/%m/%d', default='https://static.vecteezy.com/system/resources/thumbnails/005/545/335/small/user-sign-icon-person-symbol-human-avatar-isolated-on-white-backogrund-vector.jpg')
    topic = models.CharField(max_length=50)
    publish = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    
class communityList(models.Model):
    title = models.CharField(max_length=250)
    introduce = models.CharField(max_length=250)
    avatar = models.ImageField(blank=False, null=False, upload_to='images/%y/%m/%d', default='https://static.vecteezy.com/system/resources/thumbnails/005/545/335/small/user-sign-icon-person-symbol-human-avatar-isolated-on-white-backogrund-vector.jpg')

    def __str__(self):
        return self.title
    
class popularPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    images = models.ImageField(blank=False, null=False, upload_to='images/%y/%m/%d', default='https://static.vecteezy.com/system/resources/thumbnails/005/545/335/small/user-sign-icon-person-symbol-human-avatar-isolated-on-white-backogrund-vector.jpg')
    topic = models.CharField(max_length=50)
    publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
class popularService(models.Model):
    title = models.CharField(max_length=100)
    introduce = models.TextField(max_length=2000)
    images = models.ImageField(blank=False, null=False, upload_to='images/%y/%m/%d', default='https://static.vecteezy.com/system/resources/thumbnails/005/545/335/small/user-sign-icon-person-symbol-human-avatar-isolated-on-white-backogrund-vector.jpg')
    topic = models.CharField(max_length=50)

    def __str__(self):
        return self.title