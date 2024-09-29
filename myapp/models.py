from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Account(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accounts")
    posts = models.ForeignKey('Post', on_delete=models.CASCADE, related_name="PollID")


class Post(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posted_polls")
    question = models.TextField(max_length=200)
    upvote_count = models.IntegerField(validators=[MinValueValidator(0)])
    DownVote_Count = models.IntegerField(validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)

class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('follower', 'followed')  # Ensures a user can't follow the same person more than once

    def __str__(self):
        return f"{self.follower} follows {self.followed}"


