from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def root(request):
    return render(request,"index.html")