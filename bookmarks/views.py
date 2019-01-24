from django.shortcuts import render, redirect

from .models import Bookmark
from users.models import Profile
from .forms import BookmarkForm

#Imports for libraries Requests and BeautifulSoup. Needed to fetch title
import requests
import bs4

#Display bookmark form
def bookmark_form(request):
    return render(request, "bookmarks/bookmark_form.html")

#Create a bookmark
def create_bookmark(request):
    if request.method == "POST":
        form = BookmarkForm(request.POST)
        if form.is_valid():
            profile = Profile.objects.get(user=request.user)
            new_bookmark = form.save(commit=False)
            is_private = request.POST.get("private", False)

            #Fetch title if left empty
            if request.POST["title"] == "":
                title = get_title(request.POST["url"])
                new_bookmark.title = title

            #Make post private
            if is_private:
                new_bookmark.public = False

            new_bookmark.user = request.user
            new_bookmark.save()
            form.save_m2m() #Required to save tags
            profile.bookmarks.add(new_bookmark)
            return redirect("user_bookmarks")

#Fetch title from web page
def get_title(url):
    r = requests.get(url, timeout=5)
    html = bs4.BeautifulSoup(r.text)
    title = html.title.text
    return title
