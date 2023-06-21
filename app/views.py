from django.shortcuts import render

# Create your views here.



def home(request):
    return render(request,'home.html')

def regform(request):
    return render(request,'regform.html')

def loginform(request):
    return render(request,'loginform.html')