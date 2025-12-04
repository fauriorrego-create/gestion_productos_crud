from django.urls import path
from . import views

urlpatterns = [

    path('', views.listar_pedidos, name='listar_pedidos'),
    path('crear/', views.crear_pedido, name='crear_pedido'),
    path('ver/<int:pk>/', views.ver_pedido, name='ver_pedido'),
    path('actualizar/<int:pk>/', views.actualizar_pedido, name='actualizar_pedido'),
    path('eliminar/<int:pk>/', views.eliminar_pedido, name='eliminar_pedido'),
]


