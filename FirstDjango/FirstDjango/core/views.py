from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest
import random
from .models import User
# Create your views here.
def index(request):
    return render(request, 'core/index.html', {
        "random_num": random.randint(1, 100)
    })


def users(request: HttpRequest):
    return render(request, 'core/users.html', {

    })

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
