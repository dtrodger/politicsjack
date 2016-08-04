from django.contrib import admin

from .models import Cause

class CauseAdmin(admin.ModelAdmin):
	pass

admin.site.register(Cause, CauseAdmin)