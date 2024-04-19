from django.shortcuts import render
from chat.models import Message
from chat.models import Chat

# Create your views here.

def index(request): 
    if request.method == "POST":
        print("Recieved data: " + request.POST['txtmessage'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(text=request.POST['txtmessage'], chat=myChat, author=request.user, reciever=request.user)
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages': chatMessages})

def login__screen(request):
    if request.method == "POST":
        user = 
        if user:
            return HttpResponseRedirect('/chat/')
        else:
            return render(request, )
    return render(request, 'auth/login.html')