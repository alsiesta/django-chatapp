from django.contrib import admin
from .models import Message, Chat

class MessageAdmin(admin.ModelAdmin):
    fields = ('chat','text','created_at', 'author', 'receiver', )
    list_display = ('created_at','text', 'author',  'receiver', 'chat')
    search_fields = ('text',)
    
class ChatAdmin(admin.ModelAdmin):
    fields = ('created_at',)
    list_display = ('created_at',)
    search_fields = ('created_at',)

# egister your models here.
admin.site.register(Message, MessageAdmin)
admin.site.register(Chat,ChatAdmin)
