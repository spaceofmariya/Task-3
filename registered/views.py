import json

from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse

from registered.forms import RegistrationForm
from registered.models import Form


def register(request):
    form = RegistrationForm()
    context = {
        "form":form
    } 
    return render(request,"web/register.html",context=context)

def submit(request):
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    date_of_birth = request.POST.get("date_of_birth")
    gender = request.POST.get("gender")
    email = request.POST.get("email")
    contact_number = request.POST.get("contact_number")
    school_grade = request.POST.get("school_grade")
    item = request.POST.get("item")
    
    # if not Form.objects.filter(email=email).exists():
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
    # else:
    #     response_data = {
    #         "status": "error",
    #         "title": "Already registered",
    #         "message": "You have already registered using the same emailid. No multiple registrations allowed."
    #     }
    return HttpResponse(json.dumps(response_data),content_type="application/javascript")
    # if request.method == "POST":
    #     form = RegistrationForm(request.POST)
        
    #     if form.is_valid():
    #         print(form)
    #         form.save()
    #         response_data = {
    #             "status": "success",
    #             "title": "Successfully registered",
    #             "message": "You have successfully registered for the Arts Fest. Click OK to return to the Home page",
    #             "redirect": "yes",
    #             "redirect_url": "/"
    #         }
    #         return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    #     else:
    #         print("Error2")
    #         response_data = {
    #             "status": "error",
    #             "title": "Already registered",
    #             "message": "You have already registered. No multiple registrations allowed."
    #         }  
    #         return HttpResponse(json.dumps(response_data), content_type='application/javascript')

    # else:
         
    #     return render(request,"web/register.html")


# def register(request):

#     if request.method == "POST":
#         form = RegistrationForm(request.POST, request.FILES)

#         if form.is_valid():
#             print(form)
#             form.save()
#             response_data = {
#                     "title": "Successfully submitted",
#                     "message": "Successfully submitted",
#                     "status": "success",
#                     "redirect": "yes",
#                     "redirect_url": "/"
#             }
#             return HttpResponse(json.dumps(response_data), content_type='application/javascript')  
#         else:
#             print("error")
#             context={
#             "form" : form
#             }
#             return render(request,'web/register.html',context=context)
        
#     else:
#         data={
#             "first_name":"Test",
#             "last_name":"Test2",
#             "gender":"F",
#             "class_":"5",
#             "email":"test@gmail.com",
#             "contact_number":"1234567890",
#             "item":"5",
#         }
#         form = RegistrationForm(initial=data)
#         context={
#             "form" : form
#         }
#         return render(request,'web/register.html',context=context)

#Applicant form Edit function    
def edit(request,id):
    student = get_object_or_404(Form,id=id)
    print(student)
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES,instance=student)
        if form.is_valid():
            form.save()
            response_data = {
                    "title": "Successfully submitted",
                    "message": "Successfully submitted",
                    "status": "success",
                    "redirect": "yes",
                    "redirect_url": "/logged-in/"
            }
            return HttpResponse(json.dumps(response_data), content_type='application/json')  
    else:
        form = RegistrationForm(instance=student)
        context={
            "form" : form
        }
        return render(request,'web/register.html',context=context)


#Applicant form delete function
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

