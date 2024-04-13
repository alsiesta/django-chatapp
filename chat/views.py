# pylint: disable=no-member, disable=missing-function-docstring,invalid-name


from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.core import serializers

from chat.models import Message
from chat.models import Chat

@login_required(login_url='/login/')
def index(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    if request.method == 'POST':
        print('Received Data: ' + request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        new_message = Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
        serialized_obj = serializers.serialize('json', [ new_message, ])
        return JsonResponse(serialized_obj[1:-1], safe=False)
    
    chat_messages = Message.objects.filter(chat__id=1)
    last_message_date = chat_messages.last().created_at 
    last_message_date_time = last_message_date.strftime('%Y-%m-%d %H:%M:%S')   
    print('Last Message Date: ', last_message_date_time)
    
    return render(request, 'chat/index.html', {'chat_messages': chat_messages, 'last_message_date_time': last_message_date_time})


def login_view(request):
    redirect = request.GET.get('next', '/chat/')

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

    if request.method == 'POST':
        print("REGISTER REQUEST POST: ", request.POST)
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        User.objects.create_user(username=username, password=password)
        return redirect('/chat/')

    return render(request, 'auth/register.html')


def logout_view(request):
    logout(request)
    return redirect('/chat/')  # Redirect to login page after logout
