from django.contrib import admin
from models import *
# Register your models here.
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['nickname','email']
admin.site.register(Resume,ResumeAdmin)