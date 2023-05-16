from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from django.urls import reverse


class Post(models.Model):
    tweet = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tweet} {self.time_stamp}"

    def get_absolute_url(self):
        return reverse('tweet-detail', args=[str(self.pk)])
