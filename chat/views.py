# pylint: disable=no-member

from django.shortcuts import render
from chat.models import Message
from chat.models import Chat


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
