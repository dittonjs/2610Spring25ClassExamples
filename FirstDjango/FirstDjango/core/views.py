from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest
import random
from .models import User

# dont do this for real! Use a database!
USERS = []

# Create your views here.
def index(request):
    return render(request, 'core/index.html', {
        "random_num": random.randint(1, 100),
        "users": USERS
    })


def users(request: HttpRequest):
    if request.method == "POST":
        user = User(
            name=request.POST.get("name", "Default Name"),
            age=request.POST.get("age", 0),
            email=request.POST.get("email", "default@example.com")
        )
        USERS.append(user)
        return redirect('/')
    else:
        return render(request, 'core/users.html')


# FOR GET REQUEST
# def users(request: HttpRequest):
    # #validate email and name and age in the request
    # if not request.GET.get("name") or not request.GET.get("email") or not request.GET.get("age"):
    #     return HttpResponseBadRequest("Missing required parameters")
    # if "@" not in request.GET.get("email"):
    #     return HttpResponseBadRequest("Invalid email")
    # if not request.GET.get("age").isnumeric():
    #     return HttpResponseBadRequest("Invalid age")
    # if not request.GET.get("name").isalpha():
    #     return HttpResponseBadRequest("Invalid name")

    # user = User(
    #     name=request.GET.get("name", "Default Name"),
    #     age=request.GET.get("age", 0),
    #     email=request.GET.get("email", "email@example.com")
    # )

    # return render(request, 'core/users.html', {
    #     "user": user
    # })
