from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def home(request):
#     return HttpResponse("<h1>Hello Django!</h1>")

def home(request, param):
    return HttpResponse(f"<h1>Bonjour { param }!</h1>") 

def contactUs(request):
    return HttpResponse("<h1>Contact Us</h1><p>fill this form in order to contqct us</p>")

def aboutUs(request):
    return HttpResponse("<h1>About us</h1><p>We are a group of student. Nice to meet you !!</p>")