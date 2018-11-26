from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save



# Create your models here.

class SocialUser(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    b_day = models.DateField(auto_now=False, auto_now_add=False)
    password = models.CharField(max_length=255)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    friend = models.CharField(max_length=255, null=True)


    def __unicode__(self):
        return self.name + " " + self.last_name

    def __str__(self):
         return self.name + " " + self.last_name


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    author = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', null=True)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user')
    photo = models.ImageField(null=True, blank=True)
    city = models.CharField(max_length=255, null=True)
    job = models.CharField(max_length=80, null=True)


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    user = models.ForeignKey(User, related_name='user_comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(UserProfile, related_name='user_comments_photo', null=True)

    class Meta:
        ordering = ['-created']


class Interests(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    img = models.ImageField(null=True, blank=True)
    user_interests = models.ManyToManyField(User)




