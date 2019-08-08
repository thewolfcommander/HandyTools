from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login


from .forms import *


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    context = {
        'form': form
    }
    return render(request, 'signup.html', context)