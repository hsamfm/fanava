from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
# from .forms import UserProfileInfoForm, UserForm
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib import messages as message


# Create your views here.

class LoginView(View):
    template_name = 'admin/pages/examples/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            email = request.POST['email']
            password = request.POST['password']
            this_user = get_object_or_404(User, email=email)
            if check_password(password, this_user.password):
                message.info(request, "با موفقیت وارد شدید !")
                return redirect(f'/users/admin/panel/?status=true&email={email}')
            else:
                info = message.info(request, "با موفقیت وارد شدید !")
                errors = message.error(request, "ایمیل یا رمز عبور اشتباه است‌‌ !")
                return render(request, self.template_name,
                              context={'message_errors': errors, 'message_success': info})


class RegisterView(View):
    template_name = 'admin/pages/examples/register.html'

    error_messages = {
        'password_mismatch': _("پسورد ها باهم برابر نیستند !"),
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password']
            password2 = request.POST['password_conf']

            if password1 and password2 and password1 != password2:
                raise ValidationError(self.error_messages["password_mismatch"], code='password_mismatch')
            elif User.objects.filter(username=request.POST['username'], email=request.POST['email']).exists():
                return HttpResponse("Login Field!")
            else:
                u = User.objects.create_user(username, email, password1)
                u.save()
                return render(request, self.template_name,
                              context={"message": "با موفقیت ثبت نام شدید لطفا لاگین کنید !"})

        return render(request, self.template_name, context={'errors': "مثل اینکه قبلا ثبت نام کرده اید !"})


class ForgetPassword(View):
    template_name = 'forget-pass.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})

    def post(self, request, *args, **kwargs):
        pass


class AdminView(View):
    template_name = 'admin/index.html'

    # @login_required(login_url='/users/login/')
    def get(self, request):
        return render(request, self.template_name, context={})

    def post(self, request, *args, **kwargs):
        pass
