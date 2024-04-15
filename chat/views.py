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
    """
    Handles the chat index page. If the request method is POST, it creates a new message
    with the posted text message, serializes it and returns it as a JSON response.
    If the request method is not POST, it fetches all messages from the chat with id 1,
    gets the date of the last message and renders the chat index page with the messages and the last message date.

    Args:
        request (HttpRequest): The request object.

    Returns:
        JsonResponse/HttpResponse: A JSON response with the new message if the request method is POST, 
        otherwise an HttpResponse with the rendered chat index page.
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
    """
    Handles the login view. If the request method is POST, it authenticates the user with the posted username and password.
    If the user is authenticated, it logs the user in and redirects to the next page or the chat page if no next page is specified.
    If the user is not authenticated, it renders the login page with a wrong password error.
    If the request method is not POST, it renders the login page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponseRedirect/HttpResponse: A redirect to the next page or the chat page if the user is authenticated, 
        otherwise an HttpResponse with the rendered login page.
    """
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
    """
    Handles the register view. If the request method is POST, it checks if the posted username already exists.
    If the username exists, it redirects to the register page with a username already exists error.
    If the username does not exist, it checks if the posted password and confirm password match.
    If the passwords do not match, it redirects to the register page with a passwords do not match error.
    If the passwords match, it creates a new user with the posted username and password and redirects to the chat page.
    If the request method is not POST, it renders the register page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponseRedirect/HttpResponse: A redirect to the chat page if a new user is created, 
        otherwise an HttpResponse with the rendered register page.
    """
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
    """
    Logs out the user and redirects to the chat page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponseRedirect: A redirect to the chat page.
    """
    
    logout(request)
    return redirect('/chat/')  # Redirect to login page after logout
