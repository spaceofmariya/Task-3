from django.shortcuts import render

from registered.models import Form


#Function to render homepage
def index(request):
    return render(request,'web/index.html')


#Function to list the registered participants
def register(request):
    participants = Form.objects.all()
    context={
        "participants": participants
    } 
    return render(request,'users/userPage.html', context=context)


#Function to load the full detail page of each participant
def details(request,id):
    candidate = Form.objects.get(id=id)
    context = {
        "candidate": candidate    
    }
    return render(request,"signedUp/registered.html",context=context)