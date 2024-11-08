from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['c_password']
        username = request.POST['username']
        if password == c_password:
            if User.objects.filter(username = username).exists():
                messages.info(request,'Username already taken')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request,'Email already taken')
                return redirect('register')
            else:
                user =  User.objects.create_user(username = username, password = c_password, email=email, first_name = first_name, last_name= last_name)
                user.save()
                messages.info(request,'User created Successfully')
                return redirect('login')
        else:
            messages.info(request,'Confirm Password should be same as password')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')