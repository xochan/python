from __future__ import unicode_literals
from django.db import models
from datetime import date
from time import strptime
import bcrypt
from apps.login.models import User

class PostManager(models.Manager):
    def post_validator(self, requestpost):
        errors = {}
        if len(requestpost['post']) < 10:
            errors["post_10"] = "Message should be at least 10 characters"
        return errors

class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.SET_NULL,null=True)
    user_fav_post = models.ManyToManyField(User, related_name='fav_post' )
    post= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager()

class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.SET_NULL,null=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.SET_NULL,null=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Reply(models.Model):
    user = models.ForeignKey(User, related_name='replies', on_delete=models.SET_NULL,null=True)
    comment = models.ForeignKey(Comment, related_name='replies', on_delete=models.SET_NULL,null=True)
    reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
