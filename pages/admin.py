from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'subject', 'sent_at', 'is_read')
    list_filter = ('is_read', 'sent_at')
    readonly_fields = ('name', 'phone_number', 'subject', 'message', 'sent_at')
    ordering = ('-sent_at',)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, object_id)
        if obj and not obj.is_read:
            obj.is_read = True
            obj.save()
        return super().change_view(request, object_id, form_url, extra_context)
