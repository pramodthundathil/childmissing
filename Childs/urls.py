from django.urls import path 
from .import views 

urlpatterns = [
    path("FoundChild",views.FoundChild,name="FoundChild"),
    path("ViewMissingChilldUser",views.ViewMissingChilldUser,name="ViewMissingChilldUser"),
    path("DeleteFoundCase/<int:pk>",views.DeleteFoundCase,name="DeleteFoundCase"),
    path("FoundChildPoliceView",views.FoundChildPoliceView,name="FoundChildPoliceView"),
    path("ApproveFounndCase/<int:pk>",views.ApproveFounndCase,name="ApproveFounndCase"),
    path("Policecase",views.Policecase,name="Policecase"),
    path("Policecasereport",views.Policecasereport,name="Policecasereport"),
    path("firstatusupdate/<int:pk>",views.firstatusupdate,name="firstatusupdate"),
    path("CloseCaseupdate/<int:pk>",views.CloseCaseupdate,name="CloseCaseupdate"),
    path("DeleteFoundCasePolice/<int:pk>",views.DeleteFoundCasePolice,name="DeleteFoundCasePolice"),
    path("DeleteMissingChildCase/<int:pk>",views.DeleteMissingChildCase,name="DeleteMissingChildCase"),
    path("FaceRecoganition/<int:pk>",views.FaceRecoganition,name="FaceRecoganition"),

]