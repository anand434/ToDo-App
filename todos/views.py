from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo


def task(request):
    todos = Todo.objects.all()[:]

    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)


def details(request, id):
    todos = get_object_or_404(Todo, id=id)
    context = {
        'todo': todos
    }
    return render(request, 'details.html', context)


def add(request):
    if request.method == 'POST':
        # get the data
        title = request.POST["title"]
        txt = request.POST["text"]

        # push into sqlite3
        todo = Todo(title=title, text=txt)
        todo.save()
        return redirect('/')
    else:
        return render(request, 'add.html')