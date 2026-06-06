from django.contrib import admin
from .models.contact_message import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'company', 'subject', 'status', 'created_at']
    list_filter = ['status']
    search_fields = ['name', 'email', 'company', 'subject', 'message']
    ordering = ['-created_at']
    readonly_fields = ['name', 'email', 'company', 'subject', 'message', 'ip_address', 'created_at']
    list_editable = ['status']
    date_hierarchy = 'created_at'
