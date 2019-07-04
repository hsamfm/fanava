from django import forms


class PostForm(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    description = forms.CharField(max_length=100, widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))
    slug = forms.SlugField(widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
    image = forms.ImageField(allow_empty_file=True, widget=forms.FileInput(attrs={
        'class': 'form-control'
    }))
