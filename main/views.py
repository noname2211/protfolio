from django.shortcuts import render
from django.urls import path,include

# Create your views here.
from django.shortcuts import render

# Create your views here.
def root(request):
    context={
        "view": "header"


    }
    return render(request,"temp.html",context)