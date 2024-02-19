from django.shortcuts import render, redirect
from .forms import FoundChildForm, PoliceCaseForm
from django.contrib import messages
from .models import FoundChilds,MissingChilds,PoliceCase
from django.contrib.auth.decorators import login_required
from datetime import date

# Create your views here.

def FoundChild(request):
    form = FoundChildForm()
    Foundchild = FoundChilds.objects.filter(user = request.user)
    if request.method == "POST":
        form = FoundChildForm(request.POST,request.FILES)
        if form.is_valid():
            child = form.save()
            child.user = request.user
            child.save()
            messages.info(request,"Found Child Reported To Police Once Approve the FIR the Child Deatils will be Live to the application")
            return redirect("FoundChild")
        else:
            messages.error(request,"Something Wrong")
            return redirect("FoundChild")

    context = {

        "form":form,
        "Foundchild":Foundchild
    }
    return render(request,"foundchild.html",context)

@login_required(login_url="SignIn")
def DeleteFoundCase(request,pk):
    child = FoundChilds.objects.get(id = pk)
    child.Photo_Of_Child.delete()
    child.delete()
    messages.info(request,"Found case deleted")
    return redirect("FoundChild")

@login_required(login_url="SignIn")
def DeleteFoundCasePolice(request,pk):
    child = FoundChilds.objects.get(id = pk)
    child.Photo_Of_Child.delete()
    child.delete()
    messages.info(request,"Found case deleted")
    return redirect("FoundChildPoliceView")

def ViewMissingChilldUser(request):
    missingchild = MissingChilds.objects.filter(user = request.user)

    context = {
        "missingchild":missingchild
    }
    return render(request,"missingchild.html",context)


def FoundChildPoliceView(request):
    form = FoundChildForm()
    Foundchild = FoundChilds.objects.all()

    if request.method == "POST":
        form = FoundChildForm(request.POST,request.FILES)
        if form.is_valid():
            child = form.save()
            child.user = request.user
            child.save()
            messages.info(request,"Found Child Reported To Police Once Approve the FIR the Child Deatils will be Live to the application")
            return redirect("FoundChildPoliceView")
        else:
            messages.error(request,"Something Wrong")
            return redirect("FoundChildPoliceView")


    context = {
        "Foundchild":Foundchild,
        "form":form
    }

    return render(request,"viewfoundChild.html",context)

@login_required(login_url="SignIn")
def ApproveFounndCase(request,pk):
    child = FoundChilds.objects.get(id = pk)
    child.approval_status = True
    child.save()
    messages.info(request,"Missing case Approved")
    return redirect("FoundChildPoliceView")

def Policecase(request):
    form = PoliceCaseForm()
    cases = PoliceCase.objects.filter(user = request.user)

    if request.method == "POST":
        form = PoliceCaseForm(request.POST)
        if form.is_valid():
            child = form.save()
            child.user = request.user
            child.save()
            messages.info(request,"Incident Reported To Police")
            return redirect("Policecase")
        else:
            messages.error(request,"Something Wrong")
            return redirect("Policecase")

    

    context = {
        "form":form,
        "cases":cases
    }
    return render(request,"registerapolice.html",context)

def Policecasereport(request):
    cases = PoliceCase.objects.all()
    context = {
        "cases":cases

    }
    return render(request,"policecasereport.html",context)

def firstatusupdate(request,pk):
    cases = PoliceCase.objects.get(id = pk)
    if request.method == "POST":
        fir = request.POST['status']
        cases.FIR_Status = fir
        cases.approval_status = True
        cases.save()
        messages.info(request,"Data Updated")
        return redirect("Policecasereport")
    
def CloseCaseupdate(request,pk):
    cases = PoliceCase.objects.get(id = pk)
    cases.FIR_Status = "Case Closed"
    cases.status = True
    cases.save()
    messages.info(request,"Data Updated")
    return redirect("Policecasereport")
    
