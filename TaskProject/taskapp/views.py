from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from dateutil.parser import parse
from .models import Task

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

         # map variables to be one instance
        # then authenticate a user
        # authenticate requires 3 arguments --> request, username, and password
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Log a user in
            login(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            tasks = user
            return render(request, 'Todo-list_edit.html', {"tasks":tasks})
        else:
            messages.error(request,"Invalid username or password.")
    return render(request, 'login.html')

# def login_request(request):
# 	if request.method == "POST":
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
# 			if user is not None:
# 				login(request, user)
# 				messages.info(request, f"You are now logged in as {username}.")
# 				return redirect("main:homepage")
# 			else:
# 				messages.error(request,"Invalid username or password.")
# 		else:
# 			messages.error(request,"Invalid username or password.")
# 	form = AuthenticationForm()
# 	return render(request=request, template_name="main/login.html", context={"login_form":form})

# def login_user(request):
#     # Create the variables to hold incoming inputs
#     username = request.POST.get('username')
#     password = request.POST.get('password')
    
#     # map variables to be one instance
#     # then authenticate a user
#     # authenticate requires 3 arguments --> request, username, and password
#     user = authenticate(request, username=username, password=password)

#     if user is not None:
#         # Log a user in
#         login(request, user)
#         return HttpResponse("Successful login")
#     else:
#         return HttpResponse("Incorrect user<br><a href=""/"">Get back to home page</a>")

def taskView(request):
    print(request.POST)
    tasks = Task.objects.all()
    if request.method == "POST":
        print(request.POST)
        if "checkbox" in request.POST:
            checkbox = request.POST["checkbox"]
            # task = Task.objects.get(id=int(taskID))
            # Task.objects.values
            print(checkbox)
            return HttpResponseRedirect('/taskapp/taskhome/')
            # task.checkbox
        if "addTask" in request.POST:
            title = request.POST["title"]
            duedate = parse(request.POST["duedate"])
            print(duedate, type(duedate))
            task = Task(title=title, duedate=duedate) #duedate=duedate
            task.save()
            return HttpResponseRedirect('/taskapp/taskhome/')
        if "deleteTask" in request.POST:
            taskID = request.POST["deleteTask"]
            task = Task.objects.get(id=int(taskID))
            task.delete()
            return HttpResponseRedirect('/taskapp/taskhome/')
    return render(request, 'Todo-list_edit.html', {"tasks":tasks})

# def addTask(request):
#     title = request.POST['title']
#     task = Task(title=title)
#     task.save()
#     return HttpResponseRedirect('/taskapp/')

