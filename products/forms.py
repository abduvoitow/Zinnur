from django import forms
from .models import OrderRequest, PaintProduct, FootwearProduct, FurnitureProduct, FootwearOrderRequest, FurnitureOrderRequest

class OrderRequestForm(forms.ModelForm):
    class Meta:
        model = OrderRequest
        fields = ['full_name', 'phone_number', 'quantity']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
            }),
        }

class FootwearOrderRequestForm(forms.ModelForm):
    class Meta:
        model = FootwearOrderRequest
        fields = ['full_name', 'phone_number', 'quantity']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ism Familiya'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+998 90 123 45 67'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'placeholder': 'Nechta dona?'
            }),
        }

class FurnitureOrderRequestForm(forms.ModelForm):
    class Meta:
        model = FurnitureOrderRequest
        fields = ['full_name', 'phone_number', 'quantity']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ism Familiya'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'placeholder': 'Nechta dona?'
            }),
        }

class PaintProductForm(forms.ModelForm):
    class Meta:
        model = PaintProduct
        fields = ['name', 'description', 'price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Mahsulot nomi'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Mahsulot haqida to\'liq ma\'lumot'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "So'm"
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }

class FootwearProductForm(forms.ModelForm):
    class Meta:
        model = FootwearProduct
        fields = ['name', 'description', 'price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Mahsulot nomi'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Mahsulot haqida to\'liq ma\'lumot'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "So'm"
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }

class FurnitureProductForm(forms.ModelForm):
    class Meta:
        model = FurnitureProduct
        fields = ['name', 'description', 'price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Mahsulot nomi'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Mahsulot haqida to\'liq ma\'lumot'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "So'm"
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }
