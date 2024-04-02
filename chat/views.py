# pylint: disable=no-member

from django.shortcuts import render
from chat.models import Message
from chat.models import Chat


def index(request):
    print(request.method)
    if request.method == 'POST':
        print('Received Data: ' + request.POST['textmessage'])
        myChat=Chat.objects.get(id=1)
        Message.objects.create(text=request.POST['textmessage'], chat=None, author=request.user, receiver=request.user)
        
    return render(request, 'chat/index.html', {'name': 'Alexander'})
