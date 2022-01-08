from django.contrib import admin
from django.urls import path
from pendencias import views
from django.conf.urls import include


app_name = 'pendencias'
urlpatterns = [
    path('', admin.site.urls),
    path('grappelli/', include('grappelli.urls')),    
    
]
