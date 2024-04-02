from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    fields = ('text','created_at', 'author', 'receiver')
    list_display = ('created_at','text', 'author',  'receiver')
    search_fields = ('text',)

# egister your models here.
admin.site.register(Message, MessageAdmin)
