from __future__ import unicode_literals
from django.db import models
from datetime import date
from time import strptime
import bcrypt
import re
import datetime

class UserManager(models.Manager):
    def registration_validator(self, requestpost):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(requestpost['email']):
            errors['email_invalid'] = "email is invalid"
        if User.objects.filter(email=requestpost['email']):
            errors["email_inuse"] = "email already in use"
        if len(requestpost['first_name']) < 2:
            errors["first_2"] = "first name should be at least 2 characters"
        if len(requestpost['last_name']) < 2:
            errors["last_2"] = "Last name should be at least 2 characters"
        if len(requestpost['password']) < 8:
            errors["pass_5"] = "Password should be at least 8 characters"
        return errors

    def login_validator(self, requestpost):
        errors = {}
        if not User.objects.filter(email=requestpost['email_check']):
            errors['no_email']= "email doesn't exit"
        try:
            userx = User.objects.get(email=requestpost['email_check'])
            if not bcrypt.checkpw(requestpost['pass_check'].encode(), userx.password.encode()):
                errors['wrong_pass']= "wrong password, please try again"
        except:
            errors['no_email']= "email doesn't exit"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
