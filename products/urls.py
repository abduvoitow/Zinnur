from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('order/<str:product_type>/<int:product_id>/', views.order_universal, name='order_universal'),
]
