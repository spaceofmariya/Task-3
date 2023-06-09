from django.shortcuts import render,reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User

from main.functions import generate_form_errors
from users.forms import UserForm
from users.models import SignedupUser


#School official's LOGIN function 
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request,user)

                return HttpResponseRedirect("/logged-in/")
 
        context={
            "error":True,
            "message": "Invalid username or password"
        }
        return render(request, "users/login.html",context=context)
    else:
        context = {}
        return render(request, "users/login.html", context=context)
 

#School official's LOGOUT function
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("web:index"))


#School official's SIGNUP function
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)

            user = User.objects.create_user(
                username=instance.username,
                password=instance.password,
                email=instance.email,
                first_name=instance.first_name,
                last_name=instance.last_name
            )
            user.save()

            SignedupUser.objects.create(name=instance.first_name, user=user)

            user = authenticate(request,username=instance.username, password=instance.password)
            auth_login(request,user)

            return HttpResponseRedirect(reverse("web:index"))
        else:
            message = generate_form_errors(form)
               
            form = UserForm()
            context = {
                "error": True,
                "message": message,
                "form": form,
            }
            return render(request, "users/signup.html", context=context)
    else:
        form = UserForm()
        context = {
            "form": form,
        }
        return render(request, "users/signup.html", context=context)
    

