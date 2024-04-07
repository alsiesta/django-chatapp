# pylint: disable=no-member

from django.shortcuts import render, redirect
from django.contrib import messages
from chat.models import Message
from chat.models import Chat
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def index(request):
    print(request.method)
    if request.method == 'POST':
        print('Received Data: ' + request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(
            text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)

    chat_messages = Message.objects.filter(chat__id=1)
    # chat_messages = Message.objects.filter(created_at='2024-04-02')
    print(chat_messages)

    return render(request, 'chat/index.html', {'chat_messages': chat_messages})


def login_view(request):
    print("THE GET REQUEST: ", request.GET)
    redirect = request.GET.get('next')

    if request.method == 'POST':
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user:
            login(request, user)
            return HttpResponseRedirect(request.POST.get('redirect'))
        else:
            return render(request, 'auth/login.html', {'wrongPassword': True, 'redirect': redirect})
    return render(request, 'auth/login.html', {'redirect': redirect})


def register_view(request):
    print("THE GET REQUEST: ", request.GET)

    if request.method == 'POST':
        print("THE GET REQUEST: ",request.GET)
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('home')
    
    return render(request, 'auth/register.html')