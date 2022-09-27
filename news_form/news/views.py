from multiprocessing.reduction import send_handle
from urllib.request import HTTPErrorProcessor
from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm, SendEmail
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

def email_view(request):
    b= SendEmail()
    return render(request, 'news/email.html', {'f':b})

def process(request):
    if request.method == "POST":
        g = SendEmail(request.POST)
        if g.is_valid():
            tieude = g.cleaned_data['title']
            noidung = g.cleaned_data['content']
            email = g.cleaned_data['email']
            cc = g.cleaned_data['cc']
            context ={'td': tieude, 'cc': cc, 'nd': noidung, 'e': email}
            return render(request, 'news/printEmail.html', context)
        else: 
            return HttpResponse('Khong validate')
    else:
        return HttpResponse('not post')