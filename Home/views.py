from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from .forms import UserAddForm
from django.contrib import messages
from .decorators import admin_only, unautenticated_user
from Childs.models import MissingChilds, FoundChilds
from Childs.forms import MissingChildForm, FoundChildForm
from django.contrib.auth.decorators import login_required
from .models import PoliceData

# Create your views here.
@login_required(login_url="SignIn")
@admin_only
def Index(request):
    form = MissingChildForm()
    missingchild = MissingChilds.objects.filter(approval_status = True)
    Foundchild = FoundChilds.objects.filter(approval_status = True)

    if request.method == "POST":
        form = MissingChildForm(request.POST,request.FILES)
        if form.is_valid():
            child = form.save()
            child.user = request.user
            child.save()
            messages.info(request,"Missing Child Reported To Police Once Approve the FIR the Missing Add will be Live to the application")
            return redirect(Index)
        else:
            messages.error(request,"Something Wrong")
            return redirect(Index)



    context = {
        "form":form,
        "missingchild":missingchild,
        "Foundchild":Foundchild
    }
    return render(request,'index.html',context)

def AdminIndex(request):
    form = UserAddForm()
    
    police = PoliceData.objects.filter(user__groups__name = "police")

    if request.method == "POST":
        form = UserAddForm(request.POST)
        stn = request.POST["stn"]
        add = request.POST["add"]
        dis = request.POST["dis"]
        desi = request.POST["desi"]
        if form.is_valid():
            user = form.save()
            user.save()
            group = Group.objects.get(name='police')
            user.groups.add(group)
            Police = PoliceData.objects.create(Police_Station = stn,Address = add, District = dis, Designation = desi)
            Police.user = user
            Police.save()
            messages.success(request,"Police User Created.. Please Login....")
            return redirect("AdminIndex")

    context = {
        "form":form,
        "police":police
    }
    return render(request,"adminindex.html",context)

@login_required(login_url="SignIn")
def PoliceIndex(request):
    form = MissingChildForm()
    form1 = FoundChildForm()

    un_missingchild = MissingChilds.objects.filter(approval_status = False)
    missingchild = MissingChilds.objects.filter(approval_status = True)
    Foundchild = FoundChilds.objects.filter(approval_status = True)
    un_Foundchild = FoundChilds.objects.filter(approval_status = False)


    if request.method == "POST":
        form = MissingChildForm(request.POST,request.FILES)
        if form.is_valid():
            child = form.save()
            child.user = request.user
            child.save()
            messages.info(request,"Missing Child Reported To Police Once Approve the FIR the Missing Add will be Live to the application")
            return redirect("PoliceIndex")
        else:
            messages.error(request,"Something Wrong")
            return redirect("PoliceIndex")

    context = {
        "un_missingchild":un_missingchild,
        "missingchild":missingchild,
        "form":form,
        "form1":form1,
        "Foundchild":Foundchild,
        "un_Foundchild":un_Foundchild

    }
    return render(request,"policeindex.html",context)



@login_required(login_url="SignIn")
def ApproveCase(request,pk):
    child = MissingChilds.objects.get(id = pk)
    child.approval_status = True
    child.save()
    messages.info(request,"Missing case Approved")
    return redirect("PoliceIndex")


@login_required(login_url="SignIn")
def DeleteCase(request,pk):
    child = MissingChilds.objects.get(id = pk)
    child.Photo_Of_Child.delete()
    child.delete()
    messages.info(request,"Missing case deleted")
    return redirect("PoliceIndex")

@unautenticated_user
def SignIn(request):
    missingchild = MissingChilds.objects.filter(approval_status = True)

    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['pswd']
        user1 = authenticate(request, username = username , password = password)
        
        if user1 is not None:
            
            request.session['username'] = username
            request.session['password'] = password
            login(request, user1)
            return redirect('Index')
        
        else:
            messages.info(request,'Username or Password Incorrect')
            return redirect('SignIn')
    return render(request,"login.html",{"missingchild":missingchild})


@unautenticated_user
def SignUp(request):
    form = UserAddForm()
    if request.method == "POST":
       
        form = UserAddForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            group = Group.objects.get(name='user')
            user.groups.add(group)
            messages.success(request,"User Created.. Please Login....")
            return redirect("SignIn")
        
    return render(request,"register.html",{"form":form})


def SignOut(request):
    logout(request)
    return redirect('SignIn')