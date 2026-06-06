"""
URLs principales del proyecto.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('proyectos/', include('apps.projects.urls')),
    path('blog/', include('apps.blog.urls')),
    path('casos/', include('apps.cases.urls')),
    path('contacto/', include('apps.contact.urls')),
    path('dashboard/', include('apps.dashboard.urls')),
    path('api/', include('apps.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
