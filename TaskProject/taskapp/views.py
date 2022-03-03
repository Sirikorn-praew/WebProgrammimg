from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .models import Task


def taskView(request):
    tasks = Task.objects.all()
    # if request.method == "POST":
    #     if "addTask" in request.POST:
    #         title = request.POST["title"]
    #         task = Task(title=title)
    #         task.save()
    #         return redirect("/")
    #     if "deleteTask" in request.POST:
    #         taskID = request.POST["deleteTask"]
    #         task = Task.objects.get(id=int(taskID))
    #         task.delete()
    return render(request, 'main.html', {"tasks":tasks})

def addTask(request):
    title = request.POST['title']
    task = Task(title=title)
    task.save()
    return HttpResponseRedirect('/taskapp/')

