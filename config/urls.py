from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings

from projects.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('projects/', include('projects.urls')),
    path('blog/', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
