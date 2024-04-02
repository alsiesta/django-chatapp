from django.db import models
from datetime import date
from django.conf import settings

# Create your models here.

# class Chat(models.Model):
#     created_at = models.DateTimeField(default=date.today)
    

class Message(models.Model):
    text = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=date.today)
    # chat = Chat Klasse verknüpfen
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_messages_set')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver_messages_set')