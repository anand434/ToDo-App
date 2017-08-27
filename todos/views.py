from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo


def task(request):
    todos = Todo.objects.all()[:]

    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)


def details(request, id):
    todo = Todo.object.get(id=id)
    context = {
        'todo': todo
    }
    return render(request, 'details.html', context)


def add(request):
    if request.method == 'POST':
        # get the data
        title = request.POST['title']
        text = request.POST['text']

        # push into sqlite3
        todo = Todo(title=title, text=text)
        todo.save()
        return redirect('/todos')
    else:
        return render(request, 'add.html')