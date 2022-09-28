from multiprocessing.reduction import send_handle
from urllib.request import HTTPErrorProcessor
from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm, SendEmail
from django.views import View
# Create your views here.

class IndexClass(View):
    def get(self, request):
        ketqua = "1234567"
        return HttpResponse(ketqua)


# class add_news(View):
#     def get(self, request):
#         a = PostForm()
#         return render(request, 'news/form.html', {'f':a})
    
class save_post(View):

    def get(self, request):
        a = PostForm()
        return render(request, 'news/form.html', {'f':a})
        
    def post(self, request):
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse("saved")
        else: 
            return HttpResponse("don't saved")

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