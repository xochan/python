from __future__ import unicode_literals
from django.db import models
from datetime import date
from time import strptime
import bcrypt
import re
from apps.login.models import User

class Message(models.Model):
    user = models.ForeignKey(User, related_name='messages', on_delete=models.SET_NULL,null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<Dojo object: {self.first_name} ({self.id})>"

class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.SET_NULL,null=True)
    message = models.ForeignKey(Message, related_name='comments', on_delete=models.SET_NULL,null=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<Dojo object: {self.first_name} ({self.id})>"