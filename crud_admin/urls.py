from django.contrib import admin
from django.urls import path, include  # Importar include para conectar las URLs de la app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('client.urls')),  # ← Aquí se conectan las URLs de la app
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)