from __future__ import unicode_literals
from django.db import models
from datetime import date
from time import strptime

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "title should be at least 2 characters"
        if len(postData['network']) < 4:
            errors["network"] = "network should be at least 4 characters"
        # if strptime(postData['release_date'], "%Y-%m-%d") > strptime(str(date.today()), "%Y-%m-%d"):
        #     errors['release_date'] = "date must be in the past"
        if len(postData['desc']) < 5:
            errors["desc"] = "description should be at least 5 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=100)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
    def __repr__(self):
        return f"<Dojo object: {self.title} ({self.id})>"
