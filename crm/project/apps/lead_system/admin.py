from django.contrib import admin

from . import models


@admin.register(models.Lead)
class LeadAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Base info:', {'fields': ['name', 'email', 'phone', 'ip_address']}),
        ('Date info:', {'fields': ['create_at']})
    )
    readonly_fields = ['create_at', 'email', 'phone', 'ip_address']
    list_display = ['id', 'name', 'email', 'phone', 'ip_address']
    models = models.Lead


@admin.register(models.LeadSettings)
class LeadSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Base info:', {'fields': ['lead', 'email', 'phone']}),
    )
    readonly_fields = ['lead', 'email', 'phone']
    list_display = ['id', 'lead', 'email', 'phone']
    models = models.LeadSettings
