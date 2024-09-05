from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import TaskForm, InventarioForm
from .models import Task, Inventario

# Create your views here.

def home (request):
    return render(request, 'home.html')

def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html', {'form':UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],  password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('tasks')
                #return HttpResponse('User created successfully')
            except:
                return render(request, 'signup.html', {
                    'form':UserCreationForm,
                    'error': 'Existing user'
                })
        return render(request, 'signup.html', {
            'form':UserCreationForm,
            'error': 'Wrong password'
        })
    
def tasks(request):
    tasks = Task.objects.all()
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html', {
        'tasks' : tasks
    })


def addtask(request):
    if request.method == "GET":
        return render(request, 'addtask.html', {
            'form' : TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except:
            return render(request, 'addtask.html', {
            'form' : TaskForm,
            'error' : 'provide valid data'
        })


def signout(request):
    logout (request)
    return redirect('home')

def signin(request):
    if request.method == "GET":
        return render (request, 'signin.html', {
            'form': AuthenticationForm,
        })
    else: 
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None: 
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usario y/o contraseña son incorrectos'
            })
        else:
            login(request, user)
            return redirect('tasks')                


def inventario(request):
    inventario = Inventario.objects.all()
    return render(request, 'inventario.html', {
        'inventarios' : inventario
    })


def addinventario(request):
    if request.method == "GET":
        return render(request, 'addinventario.html', {
            'form' : InventarioForm
        })
    else:
        try:
            form = InventarioForm(request.POST)
            new_inventario = form.save(commit=False)
            new_inventario.usuario = request.usuario
            new_inventario.save()
            return redirect('inventario')
        except:
            return render(request, 'addinventario.html', {
            'form' : InventarioForm,
            'error' : 'provide valid data'
        })



    #title = "Hola Mundo... "
    #return render(request, 'signup.html', 
    #{'mytitle':title})

    #return HttpResponse("<h1>Hello World!<h1> <b> <h2>Hola<h2>")