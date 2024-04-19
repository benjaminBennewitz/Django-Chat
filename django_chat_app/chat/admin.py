from django.contrib import admin
from .models import Chat, Message

class MessageAdmin(admin.ModelAdmin):
    fields = ('chat', 'text','created_at', 'author', 'reciever') # Vorschau der Listenfelder in der Detailansicht des Nachrichtenobjektes
    list_display = ('created_at', 'author', 'text', 'reciever') # Fügt der Gesamtübersicht die folgenden Listenfelder hinzu
    search_fields = ('text',) # Zeigt einen Filter an, der nur innerhalb der Textzeile sucht

# Register your models here.
admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)