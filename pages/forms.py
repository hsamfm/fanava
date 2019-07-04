from django import forms
from django.forms import ValidationError
from .models import Contact
class ContactForm(forms.ModelForm):

    name = forms.CharField(label='نام', max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control p-3',
        'placeholder': 'نام خود را وارد کنید'
    }))
    email = forms.EmailField(label='آدرس ایمیل', max_length=30, widget=forms.EmailInput(attrs={
        'class': 'form-control p-3',
        'placeholder': 'ایمیل خود را وارد کنید',
        'id': 'exampleFormControlInput1'
    }))
    description = forms.CharField(label='متن پیام', max_length=500, widget=forms.Textarea(attrs={
        'class': 'form-control p-3',
        'id': 'exampleFormControlTextarea1',
        'rows': '5',
    }))


    class Meta:
        model = Contact
        fields = ['name', 'email', 'description']