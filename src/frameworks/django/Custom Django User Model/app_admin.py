from django.contrib import admin
from core.models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ['user_id', 'email', 'mobile_number', 'full_name', 'pincode']