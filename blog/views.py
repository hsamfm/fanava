from django.shortcuts import render
from django.views.generic import View
from .models import Post


# Create your views here.

class BlogView(View):
    template_name = 'blog.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
            'posts': Post.objects.all()[:3]
        })
