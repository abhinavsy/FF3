from django.shortcuts import render

# Create your views here.
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
# from .forms import MyModelForm


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('persons:person_add')
        else:
            # messages.info(request,"invalid credentials")
            return render(request,'login.html')

    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        cfpassword=request.POST['password1']
        if cfpassword == password:
            print('password matched')

            if User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return render(request,'register.html')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
                return render(request,'register.html')

            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save();
            return render(request,'login.html')

        else:
            messages.info(request,'password not matched')
            return render(request,'register.html')
        return redirect('/')

    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')



# def read_books(request):
#
#     f = MyModelForm(request.POST or None)
#     if f.is_valid():
#         f.save()
#         messages.success(request,'YOUR BOOK IS ADDED TO THE CART')
#         return redirect('/')
#     return render(request, 'form.html', {'f': f})







