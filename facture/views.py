from django.http import HttpResponse
from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.core.mail import send_mail

# Create yo views here.
from .forms import RegisterForm

def index(request):
    return render(request,'index.html', {})

 
def registerUser(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
        return redirect('login')
    context = {'form':form}
    return render(request, 'register.html',context)

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request,'Username or Password is incorrect')
        else:
            messages.info(request,'Fill out all the fields') 
    
    return render(request,'login.html', {})
 
 
def home(request):
        return render(request,'home.html', {})
 
 

def logoutUser(request):
    logout(request)
    return redirect('index')


def serviceclient(request):
    return render(request,'serviceclient.html', {})

def sendemaill(request):
    if request.method == "POST":
        username =request.POST['username']
        email =request.POST['email']
        message=request.POST['message']   
        
        send_mail(
            'Message du client: '+username+' ,adresse:'+email,#subj
             message,#msg            
            'facturet7@gmail.com',#from email
            ['belaid.zaineb01@gmail.com'],#tomail
        )
        return render(request,'serviceclient.html',{'username':username})
       
    else:
        return render(request,'serviceclient.html', {})
    
    