
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # baraye didan dokme login, logout dar page haye api baiad url paein ro vard konim
    path('api-auth/', include('rest_framework.urls')),
    path('blog/', include('blog.urls')),
    path('accounts/', include("django.contrib.auth.urls")),

]

# serving static and media for development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)