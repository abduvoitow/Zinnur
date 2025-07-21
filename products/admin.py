from django.contrib import admin
from .models import PaintProduct, OrderRequest, FootwearProduct, FurnitureProduct, FootwearOrderRequest, FurnitureOrderRequest

admin.site.register(PaintProduct)
admin.site.register(FootwearProduct)
admin.site.register(FurnitureProduct)

@admin.register(OrderRequest)
class OrderRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'product', 'quantity', 'created_at')
    list_filter = ('product',  'created_at')
    search_fields = ('full_name', 'phone_number')

@admin.register(FootwearOrderRequest)
class FootwearOrderRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'product', 'quantity', 'created_at')
    list_filter = ('product',  'created_at')
    search_fields = ('full_name', 'phone_number')

@admin.register(FurnitureOrderRequest)
class FurnitureOrderRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'product', 'quantity', 'created_at')
    list_filter = ('product', 'created_at')
    search_fields = ('full_name', 'phone_number')
