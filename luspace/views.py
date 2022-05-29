from cgitb import html
from django.http import HttpResponse
# from .models import Contact
from django.shortcuts import render

def index(request):

    return render(request,"landing_page.html")
