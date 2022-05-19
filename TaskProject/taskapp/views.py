from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from dateutil.parser import parse
from .models import Task, User

def login_user(request):
    print(request)
    print(request.POST)
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
            return HttpResponseRedirect('/taskapp/') 
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

@login_required
def taskView(request):
    print(request.POST)
    print(request.user.id)
    # tasks = Task.objects.all()
    users = User.objects.all().exclude(id=request.user.id)
    tasks = Task.objects.filter(user=request.user.id)
    tasks_inv =  Task.objects.filter(involved=request.user.id)
    # tasks_inv.inv
    print(tasks_inv)
    if request.method == "POST":
        print(request.POST)
        if "checkbox" in request.POST:
            checkbox = request.POST["checkbox"]
            task = Task.objects.get(id=int(taskID))
            task.checkbox = checkbox
            task.save()
            # Task.objects.values
            print(checkbox)
            return HttpResponseRedirect('/taskapp/')
            # task.checkbox
        if "addTask" in request.POST:
            user = request.user
            print(user, type(user))
            title = request.POST["title"]
            duedate = parse(request.POST["duedate"])
            list_involved = request.POST.getlist("involved") #request.POST["involved"]
            # print(list_involved, type(list_involved))
            # involved = User.objects.filter(username__in=list_involved) #.values("id")
            # print(involved, type(involved))
            task = Task(title=title, duedate=duedate, user=user) #, involved=involved
            task.save()
            print("b e")
            for id in list_involved:
                task.involved.add(id)
            return HttpResponseRedirect('/taskapp/')
        if "deleteTask" in request.POST:
            taskID = request.POST["deleteTask"]
            task = Task.objects.get(id=int(taskID))
            task.delete()
            return HttpResponseRedirect('/taskapp/')
    return render(request, 'taskpage.html', {"tasks":tasks, "tasks_inv":tasks_inv, "users": users})

def log_user_out(request):
    # Log user out
    logout(request)
    return HttpResponse("You've logged out<br><a href=""/"">Get back to login</a>")

# def addTask(request):
#     title = request.POST['title']
#     task = Task(title=title)
#     task.save()
#     return HttpResponseRedirect('/taskapp/')

