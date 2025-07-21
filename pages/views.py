from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm
from django.utils.http import url_has_allowed_host_and_scheme
from news.models import NewsPost

def home(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('admin_panel:orders')
    return render(request, 'pages/home.html', {'latest_news': NewsPost.objects.all().order_by('-created_at')[:3]})

def about(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('admin_panel:orders')
    return render(request, 'pages/about.html')

def contact(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('admin_panel:orders')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Xabaringiz saqlandi. Rahmat!")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = CustomLoginForm

    def get(self, request, *args, **kwargs):
        # Agar next param bor bo'lsa va foydalanuvchi login qilmagan bo'lsa, uni olib tashlab, /login/ ga redirect qilamiz
        next_url = request.GET.get('next')
        if next_url:
            # Faqat login sahifasiga qayta yo'naltiramiz
            return redirect('login')
        return super().get(request, *args, **kwargs)

    def form_invalid(self, form):
        messages.error(self.request, "Login yoki parol noto‘g‘ri!")
        return super().form_invalid(form)