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
        if User.objects.filter(username=requestpost['username']):
            errors["username_inuse"] = "user name already in use"
        if len(requestpost['first_name']) < 2:
            errors["first_2"] = "first name should be at least 2 characters"
        if len(requestpost['last_name']) < 2:
            errors["last_2"] = "Last name should be at least 2 characters"
        if len(requestpost['pass']) < 8:
            errors["pass_5"] = "Password should be at least 8 characters"
        if requestpost['pass'] != requestpost['pw'] :
            errors["pass_no_match"] = "Passwords don't match Confirm Passwords"
        try:
            today_date = datetime.datetime.strptime(datetime.date.today().strftime("%Y-%d-%m"), "%Y-%d-%m")
            birthday_date = datetime.datetime.strptime(requestpost['birthday'], "%Y-%m-%d")
            tenthteen_date = datetime.datetime.now() - datetime.timedelta(days=10 * 365.25)
            if birthday_date > today_date:
                errors['date_future'] = "birthday must be in the past"
            if birthday_date > tenthteen_date:
                errors['date_young'] = "you must be over 10 years old to register"
        except ValueError:
            errors["date_none"] = "please enter a birthday"
        return errors

    def login_validator(self, requestpost):
        errors = {}
        if not User.objects.filter(email=requestpost['email_check']):
            errors['no_email']= "email doesn't exit"
        try:
            userx = User.objects.get(email=requestpost['email_check'])
            if not bcrypt.checkpw(requestpost['pass_check'].encode(), userx.password.encode()):
                errors['wrong_pass']= "wrong password, please try agaqin"
        except:
            errors['no_email']= "email doesn't exit"
        return errors

    def friend_validator(self, requestpost):
        errors = {}
        if not User.objects.filter(username=requestpost['username']):
            errors['username_exist']= "user doesn't exit"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=150)
    birthday = models.DateField()
    admin = models.BooleanField(default=False)
    friends = models.ManyToManyField("self")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
