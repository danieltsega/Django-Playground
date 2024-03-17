from django.shortcuts import render, redirect

from .models import Task

from .forms import TaskForm
# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    tasks_done = Task.objects.filter(done=1)
    return render(request, 'index.html', {"tasks": tasks, "form": form, "tasks_done": tasks_done})

def completed(request, task_id):
    task = Task.objects.get(id=task_id)
    task.objects.update(done=1)
    task.save()
    return redirect('home')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')