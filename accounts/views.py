from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirige a la página principal
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()  # Guarda el usuario
            print(f"Usuario registrado: {usuario.username}")  # Esto debe aparecer en la terminal
            return redirect('login')  # Redirige después del registro
        else:
            print("Formulario inválido:", form.errors)  # Muestra errores en la terminal
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirige a la página principal