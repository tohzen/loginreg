from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
    return render(request, "index.html")

def register(request):
    print(request.POST)
    resultFromValidator = User.objects.register_validator(request.POST)
    print(resultFromValidator)
    if len(resultFromValidator)>0:
        for key, value in resultFromValidator.items():
            messages.error(request, value)
        return redirect('/')
    
    newUser = User.objects.create(first_name= request.POST["fname"], last_name = request.POST["lname"], email = request.POST["email"], password= request.POST["pw"])
    print(newUser.id)
    request.session['loggedinID'] = newUser.id
    
    return redirect("/success")

def home(request):
    loggedinUser = User.objects.get(id= request.session['loggedinID'])
    context = {
        'loggedinUser':loggedinUser
    }
    return render(request, "homepage.html", context)

def logout(request):
    request.session.clear()
    return redirect("/")

def login(request):
    print(request.POST)
    resultFromValidator = User.objects.loginValidator(request.POST)
    print(resultFromValidator)
    if len(resultFromValidator)>0:
        for key, value in resultFromValidator.items():
            messages.error(request, value)
        return redirect("/")
    emailMatch = User.objects.filter(email=request.POST['email'])
    request.session['loggedinID'] = emailMatch[0].id
    
        
    return redirect("/success")