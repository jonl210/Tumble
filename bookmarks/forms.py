from django.forms import ModelForm
from django import forms

from .models import Bookmark

#Bookmark model form
class BookmarkForm(ModelForm):

    #Description not required
    description = forms.CharField(required=False)

    #Title can be fetched from page
    title = forms.CharField(required=False)

    class Meta:
        model = Bookmark
        fields = ["url", "title", "description", "tags"]
