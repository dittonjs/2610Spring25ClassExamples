from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name="index"),
    path('todos', view=views.todos, name="todos"),
]
