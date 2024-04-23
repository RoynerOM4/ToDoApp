from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from .models import Task

def index(request):
    latest_task_list = Task.objects.order_by("-due_date")[:5]
    context = {"latest_task_list": latest_task_list}
    return render(request, "ToDo/index.html", context)

    
def detail(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    return render(request, "ToDo/detail.html", {"task": task})

def complete(request, task_id):
    return HttpResponse("You're completing task %s." % task_id)

def delete(request, task_id):
    return HttpResponse("You're deleting task %s." % task_id)
