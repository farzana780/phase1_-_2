from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.shortcuts import render, redirect
from authentication.models import CustomUser

# LOGIN VIEW ENDPOINT

def loginuser(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Email or password invalid!')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['Confirm_password']
        if password == confirm_password:
            if CustomUser.objects.filter(email=email):
                messages.error(request, 'Email Already Exit ')
            else:
                user = CustomUser.objects.create_user(first_name=first_name, last_name=lastname, password=password,
                                                email=email)
                user.save()
                return redirect('/')
        else:
            messages.error(request, 'Password and Confirm password not matched ')

    return render(request, 'register.html')

def logoutuser(request):
    logout(request)
    return redirect('/')

