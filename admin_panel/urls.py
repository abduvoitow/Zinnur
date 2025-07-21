from django.urls import path
from . import views
from django.shortcuts import redirect

app_name = 'admin_panel'

urlpatterns = [
    path('', lambda request: redirect('admin_panel:orders'), name='admin_root'),
    path('news/', views.news_manage, name='news_manage'),
    path('news/create/', views.news_create, name='news_create'),
    path('news/edit/<int:pk>/', views.news_edit, name='news_edit'),
    path('news/delete/<int:pk>/', views.news_delete, name='news_delete'),

    # Unified product management page
    path('products/', views.product_manage, name='product_manage'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/edit/<int:pk>/<str:product_type>/', views.product_edit, name='product_edit'),
    path('products/delete/<int:pk>/<str:product_type>/', views.product_delete, name='product_delete'),

    path('orders', views.all_orders, name='orders'),
    path('contacts/', views.contact_list, name='contact_list'),

    path('check-orders/', views.check_new_orders, name='check_new_orders'),
    path('check-orders-public/', views.check_new_orders_public, name='check_new_orders_public'),
    
    # Status o'zgartirish uchun URL'lar
    path('update-status/<str:order_type>/<int:order_id>/<str:new_status>/', views.update_order_status, name='update_order_status'),
]







