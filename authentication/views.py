from django.shortcuts import render
from .forms import RegisterForm, LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.utils import IntegrityError
from .helper.auth_user import authenticate_user
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/auth/login")
    context = {
        "user": request.user
    }
    return render(request, 'index.html', context)

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
                return HttpResponseRedirect("/")
            else:
                context.get("errors", []).append("email atau password anda salah")
    return render(request, "login.html", context)
def register_view(request):
    register_form = RegisterForm(request.POST or None, request.FILES or None)
    context = {
        "forms": register_form,
        "errors" : []
    }
    if register_form.is_valid():
        try:
            clean_data = register_form.cleaned_data
            # ausmsikan email admin tidak digunakan sebagi email user
            # is_exist_email = User.objects.get(email=clean_data['email']) is not None
            # if is_exist_email:
            #     raise IntegrityError()
            user = User.objects.create_user(
                email = clean_data['email'],
                username = clean_data['username'],
                password = clean_data['password'],
                first_name = clean_data['name'],
            )
            register_form.save()
        except IntegrityError as e:
            print(e)
            context.get("errors", []).append("Username atau email sudah terdaftar")
            print(context)
            return render(request, "register.html", context)
    
    if request.method == "POST":
        return HttpResponseRedirect("/auth")
    return render(request, "register.html", context)
