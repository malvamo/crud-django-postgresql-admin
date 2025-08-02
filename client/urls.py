from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_registros, name='lista'),               # URL raíz → Lista de registros
    path('nuevo/', views.crear_registro, name='crear'),          # URL para crear un registro
    path('editar/<int:pk>/', views.actualizar_registro, name='editar'),  # URL para editar un registro
]