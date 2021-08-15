from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def render_dashboard(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect("/")
    else:
        return render(request, "admin_templates/index.html")