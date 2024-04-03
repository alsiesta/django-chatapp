from datetime import date
from django.db import models
from django.conf import settings

# Create your models here.

class Chat(models.Model):
    created_at = models.DateField(default=date.today)
    

class Message(models.Model):
    text = models.CharField(max_length=500)
    created_at = models.DateField(default=date.today)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='chat_messages_set', default=None, blank=True, null=True) # standardwer is None, filed darf leer sein und die DB darf null sein
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_messages_set')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver_messages_set')