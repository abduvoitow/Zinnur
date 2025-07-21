from django.contrib import admin
from .models import NewsPost

@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)
