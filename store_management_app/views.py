from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from store_management_app import models

# Create your views here.
def render_login(request):
    return render(request, "auth_templates/login.html")

def perform_login(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_obj = authenticate(request, username=username, password=password)
        if user_obj is not None:
            login(request, user_obj)
            if user_obj.user_type == "1":
                return HttpResponseRedirect(reverse("render_dashboard"))
            else:
                return HttpResponseRedirect(reverse("render_user_dashboard"))
        else:
            messages.error(request, "Invalid Credentials")
            return HttpResponseRedirect("/")

def perform_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

def render_register(request):
    return render(request, "auth_templates/register.html")

def perform_register(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        print("Sign UP Initiated")
        firstname = request.POST.get("first_name")
        lastname = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm = request.POST.get("password2")
        if confirm != password:
            messages.error(request,'Invalid password confirmation')
            return HttpResponseRedirect(reverse('render_register'))
        else:
            try:
                print("Creating User")
                user_obj = models.User.objects.create_user(first_name=firstname, last_name=lastname, username=username, password=password, user_type=2)
                user_obj.save()
                messages.success(request,'User created successfully !')
                return HttpResponseRedirect(reverse('render_register'))
            except:
                messages.error(request,'User registration falied as user already exists !')
                return HttpResponseRedirect(reverse('render_register'))