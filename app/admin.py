from django.contrib import admin
from .models import RegionModel
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','email', 'region_name']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('region_name',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('region_name',)}),
    )


admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(RegionModel)