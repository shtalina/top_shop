from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('products')
    else:
        form = UserCreationForm()
    return render(request, 'account/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Обработка успешного входа пользователя
                return render(request, 'shop/products_list.html')
                # Перенаправление на главную страницу после входа
                # Обработка неверных учетных данных
                # Например, отображение сообщения об ошибке
        # Если форма не валидна или пользователь не аутентифицирован, остаемся на странице входа и отображаем ошибки
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})

@login_required
def my_view(request):
    context = {
        'user': request.user
    }
    return render(request, 'shop/base.html', context)

def my_logout(request):
    logout(request)
    return redirect('products')