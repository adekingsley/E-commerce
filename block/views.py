from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import *
from django.contrib import messages 

# Create your views here.

from .models import Product

def index(request):
    customer= Customer.objects.all()
    products = Product.objects.all()  
    context = {'products': products, 'customer': customer} 
    return render(request, 'index.html', context)


def produce(request):
    return render(request, 'produce.html')

def blank(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        if password == password2:
            if len(password) < 7:
                messages.info(request, 'Password length too short')
                request.session['message_color'] = 'red'
                return redirect('blank')
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                request.session['message_color'] = 'red'
                return redirect('blank')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                request.session['message_color'] = 'red'
                return redirect('blank')
            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                user.save() 
                messages.info(request, 'Account created successfully')
                request.session['message_color'] = 'green'
                return redirect('produce')
        else:
            messages.info(request, 'Password not the same. Please try again!')
            request.session['message_color'] = 'red'
            return redirect('blank')      
    return render(request, 'blank.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
	auth.logout(request)
	return redirect('index')

def checkout(request):
    return render(request, 'checkout.html')

def store(request):
    return render(request, 'store.html')
