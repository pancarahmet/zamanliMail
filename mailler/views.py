from django.shortcuts import render
from .tasks import *

# Create your views here.

def index(request):
    return render(request,"index.html")

def mailgonderme(request):
    result = send_test_mail.delay()
    print(result)
    return render(request,"mailgonder.html")