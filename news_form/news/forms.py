from socket import fromshare
from django import forms
from .models import POST

class PostForm(forms.ModelForm):
    class Meta: 
        model = POST
        fields = ('title', 'content','time_create',)
    
class SendEmail(forms.Form):
    title = forms.CharField(max_length=100)
    email = forms.EmailField()
    content = forms.CharField(widget = forms.Textarea)
    cc = forms.BooleanField(required=False)