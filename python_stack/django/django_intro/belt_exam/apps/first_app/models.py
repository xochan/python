from __future__ import unicode_literals
from django.db import models
from datetime import date
from time import strptime
import bcrypt
from apps.login.models import User

class QuoteManager(models.Manager):
    def quote_validator(self, requestpost):
        errors = {}
        if len(requestpost['author']) < 1:
            errors["author_2"] = "Quoted By should be at least 2 characters"
        if len(requestpost['quote']) < 9:
            errors["quote_10"] = "Message should be at least 10 characters"
        return errors

class Quote(models.Model):
    user = models.ForeignKey(User, related_name='quotes', on_delete=models.SET_NULL,null=True)
    user_favorite = models.ManyToManyField(User, related_name='favorite_quote' )
    author = models.CharField(max_length=100)
    quote = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()