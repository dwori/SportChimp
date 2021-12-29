from django.db import models

from django.contrib.auth.models import User


class Sport(models.Model):
    name = models.CharField(max_length=1024)
    description = models.CharField(max_length=1024, null=True)
    # TODO: image = models.ImageField()

    def __str__(self):
        return self.name


class Activity(models.Model):
    title = models.CharField(max_length=1024)
    description = models.CharField(max_length=1024, null=True)
    date = models.DateField()
    # TODO: location
    location = models.CharField(max_length=1024)
    is_public = models.BooleanField(default=True)
    sport_genre = models.ForeignKey(Sport, on_delete=models.PROTECT)
    created_by_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="activity_created_by_user", null=True)
    participants = models.ManyToManyField(User, related_name="participants")

    def __str__(self):
        return self.title


class Comment(models.Model):
    created_at = models.DateField()
    activity = models.ForeignKey(Activity, on_delete=models.PROTECT)
    created_by_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="comment_created_by_user", null=True)
    text = models.CharField(max_length=1024)

    def __str__(self):
        return self.text


class FriendshipRequest(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendship_requests_sent')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendship_requests_received')


class Friend(models.Model):
    to_user = models.ForeignKey(User, models.CASCADE, related_name='friends')
    from_user = models.ForeignKey(User, models.CASCADE, related_name='_unused_friend_relation')


class Profile(models.Model):
    # TODO: haha shesh
    pass


# TODO OWN USER MODEL
class UserX(models.Model):
    pass

