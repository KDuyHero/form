from urllib.request import HTTPErrorProcessor
from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
# Create your views here.

def index(request):
    return HttpResponse("hello, this is news app")

def add_news(request):
    a = PostForm()
    return render(request, 'news/form.html', {'f':a})
    
def save_post(request):
    if request.method == "POST":
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse("saved")
        else: 
            return HttpResponse("don't saved")
    else:
        return HttpResponse("no post")