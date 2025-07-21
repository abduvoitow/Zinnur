from django import forms
from .models import ContactMessage
from django.contrib.auth.forms import AuthenticationForm

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'phone_number', 'message', 'subject']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ism',
                'id': 'contact-name'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Telefon raqam',
                'id': 'contact-phone'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Xabar',
                'rows': 4,
                'id': 'contact-message'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Mavzu',
                'id': 'contact-subject'
            }),
        }





class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )
