from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Content(models.Model):
    title = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="blog_contents")
    body = models.TextField()
    published_time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-published_time',)

    def __str__(self):
        return self.title

    def getAbsoluteURL(self):
        return reverse('blog:content_detail',args=[self.slug])