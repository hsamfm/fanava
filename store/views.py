from django.shortcuts import render
from django.views.generic import *
from .models import Product
from category.models import Category

# Create your views here.

class StoreView(View):
    template_name = 'store.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
            'product': Product.objects.all(),
            'category': Category.objects.all().only('name')
        })


class StoreDetail(DetailView):
    template_name = 'product.html'

    def get(self, request, id=None, *args, **kwargs):
        return render(request, self.template_name, context={
            'product': Product.objects.filter(id=id)
        })
