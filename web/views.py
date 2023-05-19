from django.shortcuts import render

from registered.models import Form



def index(request):
    return render(request,'web/index.html')

def register(request):
    participants = Form.objects.all()
    context={
        "participants": participants
    } 
    return render(request,'users/userPage.html', context=context)

def details(request,id):
    candidate = Form.objects.get(id=id)
    context = {
        "candidate": candidate    
    }
    return render(request,"signedUp/registered.html",context=context)