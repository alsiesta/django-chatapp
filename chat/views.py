# pylint: disable=no-member

from django.shortcuts import render

from chat.models import Message

from chat.models import Chat

from django.contrib.auth import authenticate

from django.contrib.auth import login

from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def index(request):
    print(request.method)
    if request.method == 'POST':
        print('Received Data: ' + request.POST['textmessage'])
        myChat=Chat.objects.get(id=1)
        Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
        
    chat_messages = Message.objects.filter(chat__id=1)
    # chat_messages = Message.objects.filter(created_at='2024-04-02')
    print(chat_messages)
        
    return render(request, 'chat/index.html', {'chat_messages': chat_messages})

def login_view(request):
    print("THE GET REQUEST: ",request.GET)
    redirect= request.GET.get('next')
    
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user:
            login(request, user)
            return HttpResponseRedirect(request.POST.get('redirect'))
        else:
            return render(request, 'auth/login.html', {'wrongPassword': True, 'redirect': redirect})
    return render(request, 'auth/login.html', {'redirect': redirect})
