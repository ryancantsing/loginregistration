from __future__ import unicode_literals
from .models import User
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'login_reg/newindex.html')

def register(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully registered!")
    return redirect('/success')

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }    
    return redirect('/quotes', context)

def success(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'login_reg/success.html', context)
def quotes(request):
    return render(request, 'login_reg/quotes.html')
def users(request):
    return render(request, 'login_reg/userspage.html')
