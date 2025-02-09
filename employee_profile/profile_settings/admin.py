from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name','bio','location','birth_date','profile_pic']


# Register your models here.
