from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),

    path('accounts/', include('user.urls')),
    path('products/', include('product.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),

    path('api/v1/', include('api.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
