from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

class LoginView(View):
    template_name = 'admin/pages/examples/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})

    def post(self, request, *args, **kwargs):
        pass


class RegisterView(View):
    template_name = 'admin/pages/examples/register.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})

    def post(self, request, *args, **kwargs):
        if request.user.email.endswith('@gmail.com'):
            return redirect('/users/register/')
        else:
            if request.method == "POST":
                username = request.POST['username']
                email = request.POST['email']
                password = request.POST['password']
                password_conf = request.POST['password_conf']

                register = get_object_or_404(User, username, email, password, password_conf)
                if register is not User.objects.exists():
                    pass


class ForgetPassword(View):
    template_name = 'forget-pass.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})

    def post(self, request, *args, **kwargs):
        pass


class AdminView(View):
    template_name = 'admin/index.html'

    @login_required(login_url='/users/login/')
    def get(self, request):
        pass

    def post(self, request, *args, **kwargs):
        pass
