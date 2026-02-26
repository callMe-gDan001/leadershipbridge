from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register(Member)
"""
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
	list_display = ('full_name', 'membership_id', 'role', 'mobile_no', 'date_joined')
	search_fields = ('full_name', 'membership_id', 'mobile_no')
	list_filter =('ROLE_CHOICES')
	"""