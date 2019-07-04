from django.shortcuts import *
from django.views.generic import View, DetailView, DeleteView, UpdateView, CreateView, FormView
from .forms import ContactForm
from .models import Contact
from store.models import Product
import logging

logger = logging.getLogger(__name__)


# Create your views here.


class IndexView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        product = Product.objects.all()[:3]
        return render(request, self.template_name, context={
            'forms': ContactForm,
            'product': product
        })

    def post(self, request, *args, **kwargs):
        success = False
        if request.method == "POST":
            forms = ContactForm(request.POST)
            if forms.is_valid():
                cd = forms.save()
                logger.log(1, "Has Been Saved !")
                return HttpResponseRedirect('/?success=True')
        else:
            forms = ContactForm()
            if 'success' in request.GET:
                success = True
        return render(request, 'index.html', {"forms": forms, 'success': success})


class NewsAdd(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass
