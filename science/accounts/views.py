from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth



def login(request):
    if request.method == "POST":
        password = request.POST['password']
        username = request.POST['username']

        user = auth.authenticate(username=username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('profile')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')



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
                messages.info(request,'Имя пользователя уже занято')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request,'Электронное письмо уже отправлено')
                return redirect('register')
            else:
                user =  User.objects.create_user(username = username, password = c_password, email=email, first_name = first_name, last_name= last_name)
                user.save()
                messages.info(request,'Пользователь успешно создан')
                return redirect('login')
        else:
            messages.info(request,'Пароли не совпадают!')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')
    


@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {'user': request.user})
    