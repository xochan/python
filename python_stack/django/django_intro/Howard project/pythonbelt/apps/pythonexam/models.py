from __future__ import unicode_literals
from django.db import models
from datetime import date
from time import strptime
import bcrypt
from apps.logandreg1.models import *

class GroupManager(models.Manager):
    def group_validator(self, requestpost):
        errors = {}
        if len(requestpost['name']) < 4:
            errors["name"] = "Group created needs to be at least 5 characters"
        if len(requestpost['description']) < 14:
            errors["description"] = "Description of the group must be at least 15 characters"
        return errors

class Group(models.Model):
    user = models.ForeignKey(Registration, related_name='groups', on_delete=models.SET_NULL,null=True)
    joined_users = models.ManyToManyField(Registration, related_name='joined_groups')
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = GroupManager()