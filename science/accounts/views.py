from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect
from django.contrib.auth import logout

from articles.models import Article
from django import forms
from django.contrib.auth.models import User




class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }


def logout_user(request):
    logout(request)  # Выход пользователя
    return redirect('login')


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
                auth.login(request, user)
                return redirect('profile')
        else:
            messages.info(request,'Пароли не совпадают!')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')


@login_required
def profile(request):
    user_articles = Article.objects.filter(author=request.user).order_by('-created_at')  # Получаем статьи текущего пользователя
    return render(request, 'accounts/profile.html', {'user_articles': user_articles})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль успешно обновлен!')
            return redirect('profile')  # Имя URL для отображения профиля
    else:
        form = EditProfileForm(instance=request.user)
    
    return render(request, 'accounts/edit_profile.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


