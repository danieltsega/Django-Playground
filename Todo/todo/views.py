from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Task

from .forms import TaskForm
# Create your views here.

def index(request):
    tasks = Task.objects.filter(done=0)
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    tasks_done = Task.objects.filter(done=1)
    return render(request, 'index.html', {"tasks": tasks, "form": form, "tasks_done": tasks_done})

@require_POST
def completed(request, task_id):
    task = Task.objects.get(id=task_id)
    task.done = not task.done  # Toggle the done status
    task.save()
    return redirect('home')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')