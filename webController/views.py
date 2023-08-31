from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import JsonResponse
import random

@login_required
def dashboard(request):
    
    state_of_central = func_state_of_central()

    if request.method == 'GET':
        mensagem = func_resume_of_central()
        if state_of_central:
            return render(request, 'main/dashboard.html', {'ligado_desligado': 'Ligado', 'mensagens': mensagem})
        else:
            return render(request, 'main/dashboard.html', {'ligado_desligado': 'Desligado', 'mensagens': mensagem})
    

    elif request.method == 'POST':
    
        action = request.POST.get('action')

        if action == 'ligar_desligar':

            if state_of_central:
                return JsonResponse({'estado': 'Ligado'})
            else:
                return JsonResponse({'estado': 'Desligado'})

        elif action == 'evento_01':
            retorn_function = func_01()
            return JsonResponse({'mensagens': retorn_function})

        elif action == 'evento_02':
            retorn_function = func_02()
            return JsonResponse({'mensagens': retorn_function})

        elif action == 'evento_03':
            retorn_function = func_03()
            return JsonResponse({'mensagens': retorn_function})

        elif action == 'evento_04':
            retorn_function = func_04()
            return JsonResponse({'mensagens': retorn_function})

        elif action == 'evento_05':
            retorn_function = func_05()
            return JsonResponse({'mensagens': retorn_function})


def home(request):
    return render(request, 'main/home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/singup.html', {'form': form})


def func_state_of_central():
    return random.choice([True, False])

def func_resume_of_central():
    mensagem = "Tudo ok com a central"
    return mensagem

def func_01():
    mensagem = "Função 01"
    return mensagem

def func_02():
    mensagem = "Função 02"
    return mensagem

def func_03():
    mensagem = "Função 03"
    return mensagem

def func_04():
    mensagem = "Função 04"
    return mensagem

def func_05():
    mensagem = "Função 05"
    return mensagem


