from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .forms import TodoForm
from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'todo/home.html')

def SignUpUser(request):
    if request.method == 'GET':
        return render(request, 'todo/SignUpUser.html', {'form': UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
           try:
               user = User.objects.create_user(request.POST["username"], password=request.POST["password1"])
               user.save()
               login(request,user)
               return redirect(current)


           except IntegrityError:
               return render(request, 'todo/SignUpUser.html', {'form': UserCreationForm,"error":"this username has benn already taken"})



        else:
            return render(request, 'todo/SignUpUser.html', {'form': UserCreationForm,'error':'password did not match'})

@login_required
def current(request):
    todos = Todo.objects.filter(user=request.user,DateCompeleted__isnull=True)

    return render(request, 'todo/current.html',{'todos': todos})

@login_required
def LogoutUser(request):
    if request.method == "POST":
        logout(request)

        return redirect(home)


def LoginUser(request):
    if request.method == 'GET':
        return render(request, 'todo/LoginUser.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request, 'todo/LoginUser.html', {'form': AuthenticationForm , 'error':'username is not exist or password is not exist'})
        else:
            login(request,user)
            return redirect('current')

@login_required
def CreateTodo(request):
    if request.method == 'GET':
        return render(request, 'todo/CreateTodo.html', {'form': TodoForm})
    else:
        try:
            form = TodoForm(request.POST)
            newTodo = form.save(commit=False)
            newTodo.user = request.user
            newTodo = form.save()
            return redirect(current)
        except ValueError:
            return render(request, 'todo/CreateTodo.html', {'form': TodoForm, 'error':'Bad Data Entered!'})
@login_required
def each_todo(request,todo_pk):
    todo = get_object_or_404(Todo, id=todo_pk ,user=request.user)
    if request.method == "GET":
        form = TodoForm(instance=todo)
        return render(request, 'todo/each_todo.html', { 'todo':todo,'form': form})
    else:
        form = TodoForm(request.POST,instance=todo)
        form.save() #update
        return redirect(current)
@login_required
def completeTodo(request,todo_pk):
    todo = get_object_or_404(Todo, id=todo_pk ,user=request.user)
    if request.method == "POST":
        todo.DateCompeleted = timezone.now()
        todo.save()
        return redirect(current)

@login_required
def deleteTodo(request,todo_pk):
    todo = get_object_or_404(Todo , id=todo_pk , user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect(current)

@login_required
def completedTodo(request):
    todos = Todo.objects.filter(user=request.user,DateCompeleted__isnull=False)

    return render(request, 'todo/completedTodo.html',{'todos':todos} )





