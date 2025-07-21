from .models import PaintProduct, OrderRequest, FootwearProduct, FurnitureProduct, FootwearOrderRequest, FurnitureOrderRequest
from .forms import OrderRequestForm, FootwearOrderRequestForm, FurnitureOrderRequestForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

def product_list(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('admin_panel:orders')
    paint_products = PaintProduct.objects.all()
    furniture_products = FurnitureProduct.objects.all()
    footwear_products = FootwearProduct.objects.all()
    return render(request, 'products/product_list.html', {
        'paint_products': paint_products,
        'furniture_products': furniture_products,
        'footwear_products': footwear_products,
    })

def order_product(request, product_id):
    product = get_object_or_404(PaintProduct, pk=product_id)
    if request.method == 'POST':
        form = OrderRequestForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            messages.success(request, "Arizangiz qabul qilindi. Tez orada siz bilan bog'lanamiz!")
            return redirect('products:product_list')
    else:
        form = OrderRequestForm()
    return render(request, 'products/order_form.html', {'form': form, 'product': product})

def order_footwear(request, product_id):
    product = get_object_or_404(FootwearProduct, pk=product_id)
    if request.method == 'POST':
        form = FootwearOrderRequestForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            messages.success(request, "Arizangiz qabul qilindi. Tez orada siz bilan bog'lanamiz!")
            return redirect('products:product_list')
    else:
        form = FootwearOrderRequestForm()
    return render(request, 'products/footwear_order_form.html', {'form': form, 'product': product})

def order_furniture(request, product_id):
    product = get_object_or_404(FurnitureProduct, pk=product_id)
    if request.method == 'POST':
        form = FurnitureOrderRequestForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            messages.success(request, "Arizangiz qabul qilindi. Tez orada siz bilan bog'lanamiz!")
            return redirect('products:product_list')
    else:
        form = FurnitureOrderRequestForm()
    return render(request, 'products/furniture_order_form.html', {'form': form, 'product': product})

def order_universal(request, product_type, product_id):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('admin_panel:orders')
    if product_type == 'paint':
        product = get_object_or_404(PaintProduct, pk=product_id)
        form_class = OrderRequestForm
        model_name = 'paint'
    elif product_type == 'footwear':
        product = get_object_or_404(FootwearProduct, pk=product_id)
        form_class = FootwearOrderRequestForm
        model_name = 'footwear'
    elif product_type == 'furniture':
        product = get_object_or_404(FurnitureProduct, pk=product_id)
        form_class = FurnitureOrderRequestForm
        model_name = 'furniture'
    else:
        return redirect('products:product_list')

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            messages.success(request, "Arizangiz qabul qilindi. Tez orada siz bilan bog'lanamiz!")
            return redirect('products:product_list')
    else:
        form = form_class()
    return render(request, 'products/order_form.html', {'form': form, 'product': product, 'product_type': model_name})