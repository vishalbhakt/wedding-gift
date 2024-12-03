from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from .models import Users_Data

# Create your views here.
def main(request):
 return render(request,'main.html')

def aboutUs(request):
 return render(request,'about.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")

        else:
            return redirect("/")

    return redirect("/")

def logoutUser(request):
    logout(request)
    return redirect("/")

def registerUser(request):
    return render(request, "register.html")

def insert(request):
    name=request.POST['name']
    gender=request.POST['for']
    age=request.POST['age']
    motherTongue=request.POST['motherTongue']
    address=request.POST['address']
    hobby=request.POST['hobby']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']

    user=Users_Data(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress, age=age, motherTongue=motherTongue, hobby=hobby)
    user.save()
    msg = "Congrualation Your Registration has been Successfull."

    return render(request,'main.html',{'msg':msg})


def services(request):
    return render(request, "services.html")

def invitation(request):
    return render(request, "invitation.html")

def couplestory(request):
    return render(request, "couplestory.html")