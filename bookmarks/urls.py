from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create_bookmark', views.create_bookmark, name="create_bookmark"),
]
