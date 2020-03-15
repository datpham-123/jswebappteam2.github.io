from django.contrib import admin
from .models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','fullname','studentID', 'role', 'dob', 'bio', 'address', 'phone', 'image')

admin.site.register(Profile, ProfileAdmin)
