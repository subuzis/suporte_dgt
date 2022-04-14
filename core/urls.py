from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static






app_name = 'pendencias'
urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('', admin.site.urls),
    #path('/', include('core.urls')), # media core URLS 
]

# More paths/urls
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

