from __future__ import unicode_literals
from django.db import models
from datetime import date
from time import strptime
import bcrypt
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email_invalid'] = "email is invalid"
        if User.objects.filter(email=postData['email']):
            errors["email_inuse"] = "email already in use"
        if len(postData['first_name']) < 2:
            errors["first_name"] = "first name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        # if strptime(postData['release_date'], "%Y-%m-%d") > strptime(str(date.today()), "%Y-%m-%d"):
        #     errors['release_date'] = "date must be in the past"
        if len(postData['pass']) < 5:
            errors["pass"] = "Password should be at least 5 characters"
        if postData['pass'] != postData['pw'] :
            errors["pass"] = "Passwords don't match Confirm Passwords"
        
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __repr__(self):
        return f"<Dojo object: {self.first_name} ({self.id})>"