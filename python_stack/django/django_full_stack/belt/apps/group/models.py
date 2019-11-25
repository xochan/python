from __future__ import unicode_literals
from django.db import models
from datetime import date
from time import strptime
import bcrypt
from apps.login.models import User

class OrganizationManager(models.Manager):
    def organization_validator(self, requestpost):
        errors = {}
        if len(requestpost['name']) < 6:
            errors["name_5"] = "Name should be more than 5 characters"
        if len(requestpost['description']) < 11:
            errors["description_5"] = "Description should be more than 10 characters"
        return errors

class Organization(models.Model):
    user = models.ForeignKey(User, related_name='organizations', on_delete=models.SET_NULL,null=True)
    members = models.ManyToManyField(User, related_name='groups' )
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = OrganizationManager()