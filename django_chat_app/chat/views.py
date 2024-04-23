from django.http import HttpResponseRedirect
from django.shortcuts import render
from chat.models import Message
from chat.models import Chat
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
def index(request): 
    if request.method == "POST":
        print("Recieved data: " + request.POST['txtmessage'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(text=request.POST['txtmessage'], chat=myChat, author=request.user, reciever=request.user)
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages': chatMessages})

def login__screen(request):
    redirect = request.GET.get('next')
    if request.method == "POST":
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            if redirect:
                login(request, user)
                return HttpResponseRedirect(request.POST.get('redirect'))
            else:
                login(request, user)
                return HttpResponseRedirect('/chat/')
        else:
            return render(request, 'auth/login.html', {'wrongPassword':True, 'redirect':redirect})
    return render(request, 'auth/login.html', {'redirect':redirect})