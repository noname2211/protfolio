from django.shortcuts import render
from django.urls import path,include

# Create your views here.
from django.shortcuts import render

# Create your views here.

def resumeForUser(request):
    return  render(request,"resumeForUser.html")

def index(request):
    return  render(request,"index.html")
def root(request):
    context={
        "view": "header"


    }
    return render(request,"temp.html",context)


def skillsView(request):
    context={
        "view":"skills/view"
    }
    return render(request,"temp.html",context)

def skillsEdit(request):
    context={
        "view":"skills/edit"
    }
    return render(request,"temp.html",context)


def skillsInsert(request):
    context={
        "view":"skills/insert"

    }

    return render(request,"temp.html",context)



def experienceView(request):
    context={
        "view":"experience/view"
    }
    return render(request,"temp.html",context)


def experienceEdit(request):
    context={
        "view":"experience/edit"
    }
    return render(request,"temp.html",context)


def experienceInsert(request):
    context={
        "view":"experience/insert"
            }
    return render(request,"temp.html",context)



def contactsView(request):
    context={
        "view":"contacts/view"
            }
    return render(request,"temp.html",context)


def contactsEdit(request):
    context={
        "view":"contacts/edit"
            }
    return render(request,"temp.html",context)


def contactsInsert(request):
    context={
        "view":"contacts/insert"
    }
    return render(request,"temp.html",context)


def usersView(request):
    context={
        "view":"users/view"
            }
    return render(request,"temp.html",context)


def usersEdit(request):
    context={
        "view":"users/edit"
            }
    return render(request,"temp.html",context)


def usersInsert(request):
    context={
        "view":"users/insert"
    }
    return render(request,"temp.html",context)
