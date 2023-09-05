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
        message = func_resume_of_central()
        if state_of_central:
            return render(request, 'main/dashboard.html', {'Powered_On_or_Off': 'On', 'messages': message})
        else:
            return render(request, 'main/dashboard.html', {'Powered_On_or_Off': 'Off', 'messages': message})
    
    elif request.method == 'POST':
    
        action = request.POST.get('action')
        print(action)
        if action == 'on_off_button':
            if state_of_central:
                return JsonResponse({'state': 'On'})
            else:
                return JsonResponse({'state': 'Off'})

        elif action == 'event_01':
            retorn_function = func_01()
            return JsonResponse({'messages': retorn_function})

        elif action == 'event_02':
            retorn_function = func_02()
            return JsonResponse({'messages': retorn_function})

        elif action == 'event_03':
            retorn_function = func_03()
            return JsonResponse({'messages': retorn_function})

        elif action == 'event_04':
            retorn_function = func_04()
            return JsonResponse({'messages': retorn_function})

        elif action == 'event_05':
            retorn_function = func_05()
            return JsonResponse({'messages': retorn_function})


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
    message = "Everything ok with the central"
    return message

def func_01():
    message = "Function 01"
    return message

def func_02():
    message = "Function 02"
    return message

def func_03():
    message = "Function 03"
    return message

def func_04():
    message = "Function 04"
    return message

def func_05():
    message = "Function 05"
    return message


