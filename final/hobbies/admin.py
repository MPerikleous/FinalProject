from django.contrib import admin

from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Which field to display in the list instead of the def __str__(self) method
    list_display = ['name', 'age', 'sex']


admin.site.register(Hobbies)
class HobbiesAdmin(admin.ModelAdmin):
    list_display = ['name', 'users']
