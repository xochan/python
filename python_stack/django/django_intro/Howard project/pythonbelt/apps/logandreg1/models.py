from __future__ import unicode_literals
from django.db import models
import bcrypt
import re

class RegManager(models.Manager):
    def regis_validator(self, requestpost):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(requestpost['email']):
            errors['email_invalid'] = "email is invalid"
        if Registration.objects.filter(email=requestpost['email']):
            errors["email_inuse"] = "email already in use"
        if len(requestpost['name']) < 2:
            errors["name_2"] = "name should be at least 2 characters"
        if len(requestpost['pass']) < 8:
            errors["pass_5"] = "Password should be at least 8 characters"
        if requestpost['pass'] != requestpost['pw'] :
            errors["pass_no_match"] = "Passwords don't match Confirm Passwords"
        return errors

    def login_validator(self, requestpost):
        errors = {}
        if not Registration.objects.filter(email=requestpost['email_check']):
            errors['no_email']= "1email doesn't exit"
        try:
            userx = Registration.objects.get(email=requestpost['email_check'])
            if not bcrypt.checkpw(requestpost['pass_check'].encode(), userx.password.encode()):
                errors['wrong_pass']= "wrong password, please try again"
        except:
            errors['no_email']= "email doesn't exit"
        return errors

class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RegManager()
    def __repr__(self):
        return f"<Exam object: {self.name} ({self.id})>"