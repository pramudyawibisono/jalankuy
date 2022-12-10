from django.shortcuts import render
from .forms import RegisterForm, LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.utils import IntegrityError
from .helper.auth_user import authenticate_user
from django.contrib.auth.decorators import login_required
from django.db import connection

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, 'not_login.html')
    context = {
        "user": request.user
    }
    return render(request, 'auth_index.html', context)

@login_required(login_url='/auth/login')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/auth")

def login_view(request):
    login_form = LoginForm(request.POST)
    context = {
        "forms": login_form,
        "errors" : []
    }
    if request.method == 'POST':
        # TODO: handle login
        if login_form.is_valid():
            clean_data = login_form.cleaned_data
            email = clean_data['email']
            password = clean_data['password']
            user = authenticate_user(
                email=email, 
                password=password, 
            )
            if user is not None:
                print(user.username)
                login(request, user)
                if user.is_superuser:
                    return HttpResponseRedirect("/admin_home")
                return HttpResponseRedirect("/")
            else:
                context.get("errors", []).append("email atau password anda salah")
    return render(request, "login.html", context)
def register_view(request):
    register_form = RegisterForm(request.POST)
    context = {
        "errors" : [],
        "forms": register_form,
    }
    if request.method == "POST":
        if register_form.is_valid():
            try:
                clean_data = register_form.cleaned_data
                print(clean_data)
                # ausmsikan email admin tidak digunakan sebagi email user
                # is_exist_email = User.objects.get(email=clean_data['email']) is not None
                # if is_exist_email:
                #     raise IntegrityError()
                if clean_data["password"] != clean_data['conf_password']:
                    context.get("errors", []).append("Input password dan input konfirmasi password tidak sama")
                    return render(request, "register.html", context)
                user = User.objects.create_user(
                    email = clean_data['email'],
                    username = clean_data['username'],
                    password = clean_data['password'],
                    first_name = clean_data['name'],
                )
                register_form.save()
                return HttpResponseRedirect("/auth/login")
            except IntegrityError as e:
                # print(e)
                context.get("errors", []).append("Username atau email sudah terdaftar")
                # print(context)
        else:
            START_ERROR_MESSAGE = 26
            END_ERROR_MESSAGE = -11
            all_errors = [
                str(error)[START_ERROR_MESSAGE:END_ERROR_MESSAGE] for error in register_form.errors.values()
            ]
            context.get("errors", []).extend(all_errors)
            print(all_errors)
            
            
    else:
        register_form = RegisterForm()
    context["forms"] = register_form
    return render(request, "register.html", context)
