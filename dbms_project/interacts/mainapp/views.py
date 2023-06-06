from django.shortcuts import render,redirect
from .models import modelsignup

# Create your views here.
def home(request):
    # std=Student.objects.all()

    return render(request,"signup.html", {})
def success(request):
    # std=Student.objects.all()

    return render(request,"success.html", {})
def signup(request):
    if request.method=='POST':
        print("added")
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        rptpassword=request.POST.get("rpt-password")
        
        s=modelsignup()
        s.name=name
        s.email=email
        s.password=password
        
        s.save()
        return redirect("/mainapp/signup/")
    return render(request,"signup.html",{})