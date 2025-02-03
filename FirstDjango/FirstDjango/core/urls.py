from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('users/', views.users),
    path('users/<int:user_id>/', views.user)
]

# users/10/
