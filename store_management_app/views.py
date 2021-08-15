from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def render_login(request):
    return HttpResponse("Login")