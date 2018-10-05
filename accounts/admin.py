from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser,Ideator,Entrepreneur,Refral_directory

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'is_ideator', 'is_entrepreneur']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Ideator)
admin.site.register(Entrepreneur)
admin.site.register(Refral_directory)
