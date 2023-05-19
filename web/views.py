from django.shortcuts import render

from registered.models import Form



def index(request):
    return render(request,'web/index.html')

def register(request):
    students = Form.objects.all()
    context={
        "students": students
    } 
    return render(request,'users/userPage.html', context=context)