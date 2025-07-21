from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.utils import timezone
from django import forms
from django.core.paginator import Paginator

from news.models import NewsPost
from products.models import PaintProduct, OrderRequest, FootwearProduct, FurnitureProduct, FootwearOrderRequest, FurnitureOrderRequest
from pages.models import ContactMessage
from news.forms import NewsPostForm
from products.forms import PaintProductForm, FootwearProductForm, FurnitureProductForm

# Admin foydalanuvchi tekshiruvi
def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin)
def news_manage(request):
    news = NewsPost.objects.all()
    from django.core.paginator import Paginator
    paginator = Paginator(news, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'admin_panel/news_manage.html', {
        'news': page_obj.object_list,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    })

@user_passes_test(is_admin)
def news_create(request):
    form = NewsPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('admin_panel:news_manage')
    return render(request, 'admin_panel/news_form.html', {'form': form})

@user_passes_test(is_admin)
def news_edit(request, pk):
    news = get_object_or_404(NewsPost, pk=pk)
    form = NewsPostForm(request.POST or None, request.FILES or None, instance=news)
    if form.is_valid():
        form.save()
        return redirect('admin_panel:news_manage')
    return render(request, 'admin_panel/news_form.html', {'form': form, 'edit': True, 'instance': news})

@user_passes_test(is_admin)
def news_delete(request, pk):
    if request.method == 'POST':
        news = get_object_or_404(NewsPost, pk=pk)
        news.delete()
    return redirect('admin_panel:news_manage')

@user_passes_test(is_admin)
def product_manage(request):
    # Barcha mahsulotlarni olish
    paint_products = PaintProduct.objects.all()
    furniture_products = FurnitureProduct.objects.all()
    footwear_products = FootwearProduct.objects.all()
    all_products = []
    for p in paint_products:
        all_products.append({
            'id': p.id,
            'type': "Bo'yoq va laklar",
            'name': p.name,
            'description': p.description,
            'price': p.price,
            'image': p.image,
            'model': 'paint',
        })
    for p in furniture_products:
        all_products.append({
            'id': p.id,
            'type': 'Mebel',
            'name': p.name,
            'description': p.description,
            'price': p.price,
            'image': p.image,
            'model': 'furniture',
        })
    for p in footwear_products:
        all_products.append({
            'id': p.id,
            'type': 'Oyoq kiyimlar',
            'name': p.name,
            'description': p.description,
            'price': p.price,
            'image': p.image,
            'model': 'footwear',
        })
    all_products = sorted(all_products, key=lambda x: x['id'], reverse=True)

    from django.core.paginator import Paginator
    paginator = Paginator(all_products, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        form = UniversalProductForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['product_type'] == 'paint':
                PaintProduct.objects.create(
                    name=cd['name'],
                    description=cd['description'],
                    price=cd['price'],
                    image=cd['image'],
                )
            elif cd['product_type'] == 'furniture':
                FurnitureProduct.objects.create(
                    name=cd['name'],
                    description=cd['description'],
                    price=cd['price'],
                    image=cd['image'],
                )
            elif cd['product_type'] == 'footwear':
                FootwearProduct.objects.create(
                    name=cd['name'],
                    description=cd['description'],
                    price=cd['price'],
                    image=cd['image'],
                )
            return redirect('admin_panel:product_manage')
    else:
        form = UniversalProductForm()

    return render(request, 'admin_panel/product_manage.html', {
        'products': page_obj.object_list,
        'form': form,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    })

@user_passes_test(is_admin)
def product_create(request):
    if request.method == 'POST':
        form = UniversalProductForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['product_type'] == 'paint':
                PaintProduct.objects.create(
                    name=cd['name'],
                    description=cd['description'],
                    price=cd['price'],
                    image=cd['image'],
                )
            elif cd['product_type'] == 'furniture':
                FurnitureProduct.objects.create(
                    name=cd['name'],
                    description=cd['description'],
                    price=cd['price'],
                    image=cd['image'],
                )
            elif cd['product_type'] == 'footwear':
                FootwearProduct.objects.create(
                    name=cd['name'],
                    description=cd['description'],
                    price=cd['price'],
                    image=cd['image'],
                )
            return redirect('admin_panel:product_manage')
    else:
        form = UniversalProductForm()
    return render(request, 'admin_panel/product_form.html', {'form': form})

@user_passes_test(is_admin)
def product_edit(request, pk, product_type):
    # Find the correct model and instance
    if product_type == 'paint':
        model = PaintProduct
        type_label = "Bo'yoq va laklar"
    elif product_type == 'furniture':
        model = FurnitureProduct
        type_label = 'Mebel'
    elif product_type == 'footwear':
        model = FootwearProduct
        type_label = 'Oyoq kiyimlar'
    else:
        return redirect('admin_panel:product_manage')

    instance = get_object_or_404(model, pk=pk)

    if request.method == 'POST':
        # Make image field not required for edit
        form = UniversalProductForm(request.POST, request.FILES)
        form.fields['image'].required = False
        if form.is_valid():
            cd = form.cleaned_data
            instance.name = cd['name']
            instance.description = cd['description']
            instance.price = cd['price']
            # Only update image if a new one is uploaded
            if 'image' in request.FILES and request.FILES['image']:
                instance.image = request.FILES['image']
            instance.save()
            return redirect('admin_panel:product_manage')
    else:
        form = UniversalProductForm(initial={
            'product_type': product_type,
            'name': instance.name,
            'description': instance.description,
            'price': instance.price,
        })
        # Disable product_type selection on edit (readonly, but not disabled)
        form.fields['product_type'].widget.attrs['readonly'] = True
        form.fields['image'].required = False

    return render(request, 'admin_panel/product_form.html', {'form': form, 'edit': True, 'instance': instance})

@user_passes_test(is_admin)
def product_delete(request, pk, product_type):
    if request.method != 'POST':
        return redirect('admin_panel:product_manage')
    if product_type == 'paint':
        model = PaintProduct
    elif product_type == 'furniture':
        model = FurnitureProduct
    elif product_type == 'footwear':
        model = FootwearProduct
    else:
        return redirect('admin_panel:product_manage')
    instance = get_object_or_404(model, pk=pk)
    instance.delete()
    return redirect('admin_panel:product_manage')

@user_passes_test(is_admin)
def all_orders(request):
    # Get all orders from all types
    paint_orders = OrderRequest.objects.all()
    furniture_orders = FurnitureOrderRequest.objects.all()
    footwear_orders = FootwearOrderRequest.objects.all()

    # Annotate each with type and created_at for sorting
    all_orders = []
    for o in paint_orders:
        all_orders.append({
            'id': o.id,
            'type': 'paint',
            'full_name': o.full_name,
            'phone_number': o.phone_number,
            'product': o.product.name,
            'image': o.product.image,
            'quantity': o.quantity,
            'created_at': o.created_at,
            'status': o.status,
            'model': 'paint',
        })
    for o in furniture_orders:
        all_orders.append({
            'id': o.id,
            'type': 'furniture',
            'full_name': o.full_name,
            'phone_number': o.phone_number,
            'product': o.product.name,
            'image': o.product.image,
            'quantity': o.quantity,
            'created_at': o.created_at,
            'status': o.status,
            'model': 'furniture',
        })
    for o in footwear_orders:
        all_orders.append({
            'id': o.id,
            'type': 'footwear',
            'full_name': o.full_name,
            'phone_number': o.phone_number,
            'product': o.product.name,
            'image': o.product.image,
            'quantity': o.quantity,
            'created_at': o.created_at,
            'status': o.status,
            'model': 'footwear',
        })
    # Sort all orders by created_at desc
    all_orders = sorted(all_orders, key=lambda x: x['created_at'], reverse=True)

    paginator = Paginator(all_orders, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'admin_panel/all_orders.html', {
        'orders': page_obj.object_list,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    })

@user_passes_test(is_admin)
def contact_list(request):
    messages = ContactMessage.objects.order_by('-sent_at')
    return render(request, 'admin_panel/contacts.html', {'messages': messages})

# Status o'zgartirish uchun view'lar
@user_passes_test(is_admin)
def update_order_status(request, order_id, order_type, new_status):
    if request.method == 'POST':
        try:
            if order_type == 'paint':
                order = get_object_or_404(OrderRequest, id=order_id)
            elif order_type == 'furniture':
                order = get_object_or_404(FurnitureOrderRequest, id=order_id)
            elif order_type == 'footwear':
                order = get_object_or_404(FootwearOrderRequest, id=order_id)
            else:
                return JsonResponse({'error': 'Invalid order type'}, status=400)
            
            order.status = new_status
            order.save()
            
            return JsonResponse({'success': True, 'new_status': new_status})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@user_passes_test(is_admin)
def check_new_orders(request):
    # Barcha turdagi yangi buyurtmalarni hisoblash
    paint_orders = OrderRequest.objects.filter(status='yangi').count()
    furniture_orders = FurnitureOrderRequest.objects.filter(status='yangi').count()
    footwear_orders = FootwearOrderRequest.objects.filter(status='yangi').count()
    
    # Jami yangi buyurtmalar
    total_new_orders = paint_orders + furniture_orders + footwear_orders
    
    return JsonResponse({
        'new_count': total_new_orders,
        'paint_orders': paint_orders,
        'furniture_orders': furniture_orders,
        'footwear_orders': footwear_orders
    })

def check_new_orders_public(request):
    # Barcha turdagi yangi buyurtmalarni hisoblash
    paint_orders = OrderRequest.objects.filter(status='yangi').count()
    furniture_orders = FurnitureOrderRequest.objects.filter(status='yangi').count()
    footwear_orders = FootwearOrderRequest.objects.filter(status='yangi').count()
    
    # Jami yangi buyurtmalar
    total_new_orders = paint_orders + furniture_orders + footwear_orders
    
    return JsonResponse({
        'new_count': total_new_orders,
        'paint_orders': paint_orders,
        'furniture_orders': furniture_orders,
        'footwear_orders': footwear_orders
    })

class UniversalProductForm(forms.Form):
    PRODUCT_TYPE_CHOICES = [
        ('paint', "Bo'yoq va laklar"),
        ('furniture', 'Mebel'),
        ('footwear', 'Oyoq kiyimlar'),
    ]
    product_type = forms.ChoiceField(choices=PRODUCT_TYPE_CHOICES, label="Mahsulot turi")
    name = forms.CharField(max_length=100, label="Nomi")
    description = forms.CharField(widget=forms.Textarea, label="Tavsif")
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Narxi")
    image = forms.ImageField(label="Rasm", required=False, widget=forms.ClearableFileInput(attrs={'clearable': False}))
