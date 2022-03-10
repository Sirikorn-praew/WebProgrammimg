from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .models import Task


def taskView(request):
    print(request.POST)
    tasks = Task.objects.all()
    if request.method == "POST":
        if "checkbox" in request.POST:
            checkbox = request.POST["checkbox"]
            task = Task.objects.get(id=int(taskID))
            print(checkbox,taskID)
            return HttpResponseRedirect('/taskapp/taskhome/')
            # task.checkbox
        if "addTask" in request.POST:
            title = request.POST["title"]
            task = Task(title=title)
            task.save()
            return HttpResponseRedirect('/taskapp/taskhome/')
        if "deleteTask" in request.POST:
            taskID = request.POST["deleteTask"]
            task = Task.objects.get(id=int(taskID))
            task.delete()
            return HttpResponseRedirect('/taskapp/taskhome/')
    return render(request, 'main.html', {"tasks":tasks})

# def addTask(request):
#     title = request.POST['title']
#     task = Task(title=title)
#     task.save()
#     return HttpResponseRedirect('/taskapp/')

