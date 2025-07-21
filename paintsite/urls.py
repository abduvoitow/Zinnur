from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),        # 👈 Asosiy sahifalar (pages)
    path('products/', include('products.urls')),  # Mahsulotlar
    path('news/', include('news.urls')), # Yangiliklar
    path('admin-panel/', include('admin_panel.urls')), #Admin panel
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
