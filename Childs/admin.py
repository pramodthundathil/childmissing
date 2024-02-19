from django.contrib import admin
from .models import *
from Home.models import *
# Register your models here.
admin.site.register(MissingChilds)
admin.site.register(FoundChilds)
admin.site.register(PoliceData)
admin.site.register(PoliceCase)



