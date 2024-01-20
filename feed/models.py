from django.db import models
from django.contrib.auth.models import User

class NewTweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    tweet = models.TextField()

    def __str__(self):
        return self.tweet

