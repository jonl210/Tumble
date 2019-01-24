from django.db import models
from django.contrib.auth.models import User

from bookmarks.models import Bookmark

#Profile model for users
class Profile(models.Model):
    user = models.OneToOneField(User, null=True)
    bookmarks = models.ManyToManyField(Bookmark)
