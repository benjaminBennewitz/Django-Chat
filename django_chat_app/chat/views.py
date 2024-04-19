from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == "POST":
        print("Recieved data: " + request.POST['txtmessage'])
    return render(request, 'chat/index.html', {'username':'Ben'})