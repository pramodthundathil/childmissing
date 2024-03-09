from django.urls import path 
from .import views  

urlpatterns = [

    path("Index",views.Index,name="Index"),
    path("SignUp",views.SignUp,name="SignUp"),
    path("",views.SignIn,name="SignIn"),
    path("SignOut",views.SignOut,name="SignOut"),
    path("AdminIndex",views.AdminIndex,name="AdminIndex"),
    path("PoliceIndex",views.PoliceIndex,name="PoliceIndex"),
    path("ApproveCase/<int:pk>",views.ApproveCase,name="ApproveCase"),
    path("DeleteCase/<int:pk>",views.DeleteCase,name="DeleteCase"),
    path("SocialIndex",views.SocialIndex,name="SocialIndex"),
   
    
]  