from django.contrib import admin

from . import models


@admin.register(models.Lead)
class LeadAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Base info:', {'fields': ['name', 'email', 'phone', 'ip_address']}),
        ('Date info:', {'fields': ['create_at']})
    )
    readonly_fields = ['create_at']
    list_display = ['name', 'email', 'phone', 'ip_address']
    models = models.Lead
