from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

from .forms import SignUpForm


def home(request):
    # verificar se o usuário está logado
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # autenticar o usuário
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso')
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha inválidos')
            return redirect('home')
    return render(request, 'home.html', {})


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            # autenticação do usuário
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'Usuário cadastrado com sucesso')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})