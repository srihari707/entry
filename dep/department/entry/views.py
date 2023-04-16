from urllib import request

from django.contrib import auth
from django.contrib import messages
# from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Contact
from django.http import JsonResponse


# Create your views here.
def home(request):

    return render(request,"index.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usrr = auth.authenticate(username=username, password=password)

        if usrr is not None:
            auth.login(request, usrr)
            return redirect('entry:form')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('entry:login')


    else:
        return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        passsword1 = request.POST['passwordd']
        if password == passsword1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('registr')

            else:
                user = User.objects.create_user(username=username, password=password,
                                                )
                user.save()
                return redirect('entry:login')
        else:
            messages.info(request,'password is not matching')
            return redirect('entry:register')




    else:
        return render(request, "register.html")






def message(request):

     return render(request,"message.html")

def form(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        department = request.POST['department']
        course = request.POST['course']
        notebook = request.POST.get('notebook', False)
        pen = request.POST.get('pen', False)
        papers = request.POST.get('papers', False)

        contact = Contact(name=name, dob=dob, age=age, gender=gender, phone=phone, email=email, department=department, course=course, notebook=notebook,pen=pen, papers=papers)
        contact.save()

        return redirect('entry:message')

    else:
        return render(request, "form.html")

