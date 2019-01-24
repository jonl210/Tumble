from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from taggit.managers import TaggableManager

#Bookmark model with tags from taggit
class Bookmark(models.Model):
    user = models.ForeignKey(User, null=True)
    url = models.TextField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(default=datetime.now)
    tags = TaggableManager()
    public = models.BooleanField(default=True)
