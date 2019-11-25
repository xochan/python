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
    user_favorite = models.ManyToManyField(User, related_name='favorite_post' )
    post= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager()