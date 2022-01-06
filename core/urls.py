from django.contrib import admin
from django.urls import path
from pendencias import views



#app_name = 'pendencias'
urlpatterns = [
    path('', admin.site.urls),
    
]
