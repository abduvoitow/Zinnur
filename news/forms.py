from django import forms
from .models import NewsPost

class NewsPostForm(forms.ModelForm):
    class Meta:
        model = NewsPost
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 6
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }