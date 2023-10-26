from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
from django.urls import reverse

class newArticle(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True, null=False)
    content = models.TextField(max_length=2000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    thumbnail = models.ImageField(blank=True, null=True, upload_to='images/%y/%m/%d', default='https://static.vecteezy.com/system/resources/thumbnails/005/545/335/small/user-sign-icon-person-symbol-human-avatar-isolated-on-white-backogrund-vector.jpg')
    #images = models.ImageField(blank=True, null=True, upload_to='images/%y/%m/%d')
    topic = models.CharField(max_length=50)
    published_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-published_date',)
    
    def __str__(self):
        return f"{self.title} - {self.author}"
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):  # new
        self.slug = slugify(self.title)
        super(newArticle, self).save(*args, **kwargs)

class blogComment(models.Model):
    article = models.ForeignKey(newArticle, related_name="comments", on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return f"{self.name} - {self.created_at}"