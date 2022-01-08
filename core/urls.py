from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from pendencias import views



#app_name = 'pendencias'
urlpatterns = [
    #path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('', admin.site.urls),
    
]
