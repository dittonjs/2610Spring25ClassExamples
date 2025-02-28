from django.shortcuts import render
from .middleware import cookie_logger_middleware
# Create your views here.

@cookie_logger_middleware
def index(request):
    num_visits = int(request.COOKIES.get('num_visits', "0")) + 1
    res = render(request, 'core/index.html', {"num_visits": num_visits})
    res.set_cookie('num_visits', f"{num_visits}", httponly=True)
    return res