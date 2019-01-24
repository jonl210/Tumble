from django.shortcuts import render

#Render home page
def index(request):
    if request.user.is_authenticated:
        return render(request, "home/layout.html")
    else:
        return render(request, "home/index.html")

#Render log in page
def log_in(request):
    return render(request, "home/log_in.html")
