from django.contrib import admin
from django.urls import path, include
from config.views import index
from django.conf.urls.static import static
from config import settings

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('blog/', include('apps.blog.urls')),
    path('catalog/', include('apps.catalog.urls')),
    path('user/', include('apps.user.urls')),
    path('order/', include('apps.order.urls')),
    path('api/', include('apps.api.urls')),
    path('about/', include('apps.about.urls')),
    path('more/', include('apps.more.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)