from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"home.html")

def signup(request):
    return render(request,'signup.html')

def loginpage(request):
    return render(request,'login.html')

def add(request):
    return render(request,'add.html')

def delete(request,id):
    pass

def logout_user(request):
    return render(request,'login.html')