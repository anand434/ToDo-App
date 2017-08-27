from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

def task(request):
    todos = Todo.objects.all()[:]

    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)