import json

from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse

from registered.forms import RegistrationForm
from registered.models import Form


#Participant Registration Function
def register(request):   
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        date_of_birth = request.POST.get("date_of_birth")
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        contact_number = request.POST.get("contact_number")
        school_grade = request.POST.get("school_grade")
        item = request.POST.get("item")   

        Form.objects.create(
            first_name = first_name,
            last_name = last_name,
            date_of_birth = date_of_birth,
            gender = gender,
            email = email,
            contact_number = contact_number,
            school_grade = school_grade,
            item = item
        ) 
        response_data = {
            "status": "success",
            "title": "Successfully registered",
            "message": "You have successfully registered for the Arts Fest. Click OK to return to the Home page",
            "redirect": "yes",
            "redirect_url": "/"
        }
        return HttpResponse(json.dumps(response_data),content_type='application/javascript')
        
    else: 
        form = RegistrationForm()
        context = {
            "form":form
        } 
        return render(request,"web/register.html",context=context)


#Participant data EDIT function  
def edit(request,id): 
    participant = get_object_or_404(Form,id=id) 
    print(participant)
    if request.method == "POST":
            print("post method")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            date_of_birth = request.POST.get("date_of_birth")
            gender = request.POST.get("gender")
            email = request.POST.get("email")
            contact_number = request.POST.get("contact_number")
            school_grade = request.POST.get("school_grade")
            item = request.POST.get("item") 

            participant.first_name = first_name
            participant.last_name = last_name
            participant.date_of_birth = date_of_birth
            participant.gender = gender
            participant.email = email
            participant.contact_number = contact_number
            participant.school_grade = school_grade
            participant.item = item

            participant.save()
           

            response_data = {
                "title": "Update success",
                "message": "Successfully updated the data",
                "status": "success",
                "redirect": "yes",
                "redirect_url": "/logged-in/"
            }
            return HttpResponse(json.dumps(response_data),content_type="application/javascript")
    else:
        form = RegistrationForm(instance=participant)
        context={
            "form" : form,
        }
        return render(request,'web/register.html',context=context)


#Participant DELETE function
def delete(request,id):
    student = get_object_or_404(Form,id=id)
    student.delete()
    response_data = {
        "title": "Successfully Deleted",
        "message": "Application Successfully Deleted",
        "status": "success",
        "redirect": "yes",
    }
    return HttpResponse(json.dumps(response_data), content_type='application/json')            

