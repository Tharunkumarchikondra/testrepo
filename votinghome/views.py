from http.client import HTTPResponse
from smtplib import SMTPResponseException
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("This is my voting homepage")