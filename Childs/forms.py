from django.forms import ModelForm , TextInput, Select
from .models import MissingChilds, FoundChilds, PoliceCase
from datetime import date

today = date.today()


class MissingChildForm(ModelForm):
    class Meta:
        model = MissingChilds
        fields = ["Child_Name","Age_of_Child","Phone_number","Identification_Mark","Description","Address","District","Missing_From","Missing_Date","Photo_Of_Child"]

        widgets = {
                "Child_Name":TextInput(attrs={"class":"form-control"}),
                "Age_of_Child":TextInput(attrs={"class":"form-control","type":"number"}),
                "Phone_number":TextInput(attrs={"class":"form-control","type":"number"}),
                "Identification_Mark":TextInput(attrs={"class":"form-control"}),
                "Description":TextInput(attrs={"class":"form-control"}),
                "Address":TextInput(attrs={"class":"form-control"}),
                "District":TextInput(attrs={"class":"form-control"}),
                "Missing_From":TextInput(attrs={"class":"form-control"}),
                "Missing_Date":TextInput(attrs={"class":"form-control","type":"date","max":str(today)}),
                # "Photo_Of_Child":TextInput(attrs={"class":"form-control","type":"file"}),
        }

class FoundChildForm(ModelForm):
    class Meta:
        model = FoundChilds
        fields = ["Child_Name","Age_of_Child","Phone_number","Identification_Mark","Description","Address","District","Find_From","Found_Date","Photo_Of_Child"]

        widgets = {
                "Child_Name":TextInput(attrs={"class":"form-control"}),
                "Age_of_Child":TextInput(attrs={"class":"form-control","type":"number","min":"1"}),
                "Phone_number":TextInput(attrs={"class":"form-control","type":"number"}),
                "Identification_Mark":TextInput(attrs={"class":"form-control"}),
                "Description":TextInput(attrs={"class":"form-control"}),
                "Address":TextInput(attrs={"class":"form-control"}),
                "District":TextInput(attrs={"class":"form-control"}),
                "Find_From":TextInput(attrs={"class":"form-control"}),
                "Found_Date":TextInput(attrs={"class":"form-control","type":"date","max":str(today)}),
                # "Photo_Of_Child":TextInput(attrs={"class":"form-control","type":"file"}),
        }


class PoliceCaseForm(ModelForm):
    class Meta:
        model = PoliceCase
        fields = ["PoliceStation","Address","District","Insident_Date","Compliant"]

        widgets = {
                "PoliceStation":Select(attrs={"class":"form-control"}),
                "Address":TextInput(attrs={"class":"form-control"}),
                "District":TextInput(attrs={"class":"form-control"}),
                "Compliant":TextInput(attrs={"class":"form-control"}),
                "Insident_Date":TextInput(attrs={"class":"form-control","type":"date","max":str(today)}),
                # "Photo_Of_Child":TextInput(attrs={"class":"form-control","type":"file"}),
        }
