import json

from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse

from registered.forms import RegistrationForm
from registered.models import Form


def registration_form(request):

    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)

        if form.is_valid():
            print(form)
            form.save()
            response_data = {
                    "title": "Successfully submitted",
                    "message": "Successfully submitted",
                    "status": "success",
                    "redirect": "yes",
                    "redirect_url": "/"
            }
            return HttpResponse(json.dumps(response_data), content_type='application/json')  
        else:
            print("error")
            context={
            "form" : form
            }
            return render(request,'web/register.html',context=context)
        
    else:
        data={
            "first_name":"Test",
            "last_name":"Test2",
            "gender":"F",
            "class_":"5",
            "email":"test@gmail.com",
            "contact_number":"1234567890",
            "item":"5",
        }
        form = RegistrationForm(initial=data)
        context={
            "form" : form
        }
        return render(request,'web/register.html',context=context)

# Applicant form Edit function    
# def edit(request,id):
#     student = get_object_or_404(Form,id=id)
#     print(student)
#     if request.method == "POST":
#         form = RegistrationForm(request.POST, request.FILES,instance=student)
#         if form.is_valid():
#             form.save()
#             response_data = {
#                     "title": "Successfully submitted",
#                     "message": "Successfully submitted",
#                     "status": "success",
#                     "redirect": "yes",
#                     "redirect_url": "/userPage/"
#             }
#             return HttpResponse(json.dumps(response_data), content_type='application/json')  
#     else:
#         form = RegistrationForm(instance=student)
#         context={
#             "form" : form
#         }
#         return render(request,'web/form.html',context=context)


# Applicant form delete function
# def delete(request,id):
#     student = get_object_or_404(Form,id=id)
#     student.delete()
#     response_data = {
#                         "title": "Successfully Deleted",
#                         "message": "Application Successfully Deleted",
#                         "status": "success",
#                         "redirect": "yes",
#                     }
#     return HttpResponse(json.dumps(response_data), content_type='application/json')            
