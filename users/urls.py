from django.conf.urls import url
from . import views

from bookmarks import views as bookmarks_views

urlpatterns = [
    url(r'^bookmarks/private', views.user_private_bookmarks, name="private_bookmarks"),
    url(r'^bookmarks/public', views.user_public_bookmarks, name="public_bookmarks"),
    url(r'^bookmarks', views.user_bookmarks, name="user_bookmarks"),
    url(r'^add-bookmark', bookmarks_views.bookmark_form, name="bookmark_form"),
    url(r'^account', views.account, name="account"),
    url(r'^log-in-user', views.log_in_user, name="log_in_user"),
    url(r'^log-out-user', views.log_out_user, name="log_out_user"),
    url(r'^sign-up', views.sign_up, name="sign_up"),
]
