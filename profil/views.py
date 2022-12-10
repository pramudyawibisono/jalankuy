from django.shortcuts import render
from authentication.models import UserAccount
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .forms import EditProfileForm,EditPasswordForm
import smtplib
# Create your views here.

@login_required(login_url="/auth/login")
def edit_profile(request):
    context = {
        "errors": [],
        "success": False,
    }
    if request.method == "POST":
        try:
            instance = UserAccount.objects.get(username=str(request.user))
            form = EditProfileForm(request.POST, request.FILES, instance=instance)
            if form.is_valid():
                form.save()
                request.user.first_name = form.cleaned_data["name"]
                request.user.save()
                context["success"] = True
        except Exception as e:
            print("Error Terjadi\n\t",e)
            context.get("errors", []).append(str(e))
    else:
        form = EditProfileForm()
    context["forms"] = form
    return render(request, "edit_profile.html", context)

@login_required(login_url="/auth/login")
def index(request):
    context = {}
    try:
        user = UserAccount.objects.get(username=request.user)
        context = {
            "name": user.name,
            "email": user.email,
            "username": user.username,
            "phone": user.phone,
            "photo": user.photo,
        }
    except Exception as e:
        context.get("errors", []).append(str(e))
    return render(request, "profile.html", context)


@login_required(login_url="/auth/login")
def edit_password(request):
    context = {
        "errors": [],
        "success": False,
    }
    if request.method == 'POST':
        userAccount = UserAccount.objects.get(username=str(request.user))
        curr_password = userAccount.password
        form = EditPasswordForm(request.POST, instance=userAccount)
        if form.is_valid():
            try:
                old_password = form.cleaned_data["old_password"]
                new_password = form.cleaned_data["password"]
                conf_password = form.cleaned_data["conf_password"]
                
                if new_password != conf_password:
                    context.get("errors", []).append("Input password dan input konfirmasi password tidak sama")
                elif old_password != curr_password:
                    context.get("errors", []).append("Password lama tidak sesuai dengan password sebelumnya")
                else:
                    user = User.objects.get(username=request.user)    
                    user.set_password(form.cleaned_data["password"])
                    update_session_auth_hash(request, user)
                    form.save()
                    user.save()
                    context["success"] = True
                    logout(request)
                    return HttpResponseRedirect("/auth/login")
            except Exception as e:
                print(e)
                context.get("errors", []).append(str(e))
    else:
        form = EditPasswordForm()
    context["forms"] = form
    return render(request, "edit_password.html", context)

@login_required(login_url="/auth/login")
def lupa_password(request):
    context = {
        "errors": [],
        "success": False,
        "email" : request.user.email
    }
    if request.method == "POST":
        try:
            userAccount = UserAccount.objects.get(username=str(request.user))
            send_mail(
                subject="JalanKuy | Lupa Password", 
                message=f"Haloo {userAccount.name}\nIni password lama anda: {userAccount.password}\n\nSalam, \n\nAdmin JalanKuy", 
                from_email="noreply@jalankuy.com", 
                recipient_list=[userAccount.email],
                fail_silently=False)
            context["success"] = True
        except  smtplib.SMTPException as err:
            context.get("errors", []).append(str(err))
        except Exception as e:
            context.get("errors", []).append(str(e))
    return render(request, "lupa_password.html", context)