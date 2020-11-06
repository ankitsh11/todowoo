from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .forms import TodoForm




def homepage(request):
    return render(request, 'todo/home.html')




def signpage(request):
    if request.method == 'GET':
        return render(request, 'todo/loginpage.html', {'form':UserCreationForm()})

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect(current)

            except IntegrityError:
                return render(request, 'todo/loginpage.html', {'form':UserCreationForm(),'error':'Username already exists. Please try another username.'})

        else:
            return render(request, 'todo/loginpage.html', {'form':UserCreationForm(),'error':'Your passwords do not match'})




def authenticateUser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginpage.html', {'form':AuthenticationForm()})
    else:
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])

        if user is None:
            return render(request, 'todo/loginpage.html', {'form':AuthenticationForm(),'error':' Invalid username and password'})
        else:
                login(request, user)
                return redirect(current)



def createtodo(request):
    if request.method == 'GET':
        return render(request, 'todo/create.html', {'form':TodoForm()})
    else:
        try:
            createdata=TodoForm(request.POST)
            form=createdata.save(commit=False)
            form.user=request.user
            form.save()
            return redirect(current)
        except ValueError:
            return render(request, 'todo/create.html', {'form':TodoForm(),'error':'Value error. Please check the input!'})



def logoutuser(request):
    if request.method=='POST':
        logout(request)
        return redirect(homepage)




def current(request):
    return render(request, 'todo/currentpage.html')
