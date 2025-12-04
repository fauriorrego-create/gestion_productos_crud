from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pedidos/', include('pedidos.urls')),
    path('', lambda request: redirect('pedidos/')),
]