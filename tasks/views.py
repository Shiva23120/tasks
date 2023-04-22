from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from tasks.forms import TaskForm , CommentForm ,CustomUserCreationForm, CategoryForm
from django.contrib.auth.decorators import login_required
from tasks.models import Task,Comment

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout
# Create your views here.

def tasks(request):
    form=CategoryForm()
    profile =request.user
    if request.method=='POST':   
        taskobj=profile.tasks.filter(status=request.POST['status'])
    else:
        taskobj=profile.tasks.filter(user=request.user)
    
    return render (request,'tasks.html',{'tasks':taskobj,'form':form})

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('tasks')

    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, "user doesn't exist")
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('tasks')

        else:
            messages.error(request, "usename or password is incorrect")

    return render(request,'login_register.html')

def registerUser(request):
    form=CustomUserCreationForm()   
    
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            messages.success(request,'user sucessfully created')
            return redirect('login')
        else:
            messages.success(request,'something went wrong ')
    context={'data':'register','form':form}
    return render(request,'login_register.html',context)

 
def logoutUser(request):
    logout(request)
    messages.error(request, "been loggedout ")
    return redirect('login')
@login_required(login_url='login')
def task (request,pk):
    taskobj=Task.objects.get(id=pk)
    return render(request,'task_detailedView.html',{'task':taskobj})
@login_required(login_url='login')
def addtask(request):

    profile =request.user

    form=TaskForm()

    if request.method=='POST':


        form=TaskForm(request.POST)

        if form.is_valid():

            project=form.save(commit=False)
            project.user=profile
            project.save()
            return redirect('tasks')
        else:
            print("----------------------------form is in valid ")
    content ={'form':form}
    return render(request,'taskform.html',content)
@login_required(login_url='login')
def updatetask (request,pk):
    profile =request.user
    project=Task.objects.get(id=pk)
    form=TaskForm(instance=project)
    if request.method=='POST':
        form=TaskForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    content ={'form':form}
    return render (request,'taskform.html',content)
@login_required(login_url='login')
def deletetask (request,pk):
    profile =request.user
    project=Task.objects.get(id=pk)
    if request.method=="POST":
        project.delete()
        return redirect('tasks')
    content ={'object':project}
    return render (request,'delete-template.html',content)
