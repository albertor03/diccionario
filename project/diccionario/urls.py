from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buscar/', views.busqueda, name='busqueda'),
    path('buscar', views.busqueda, name='busqueda'),
    path('diccionario/<str:letra>/', views.diccionario, name='diccionario'),
    path('diccionario/<str:letra>', views.diccionario, name='diccionario'),
    path('termino/<str:termino>/', views.ver, name='ver'),
    path('termino/<str:termino>', views.ver, name='ver'),
    path('agregar-termino/', views.agregar_termino, name='agregar_termino'),
    path('agregar-termino', views.agregar_termino, name='agregar_termino'),
    path('editar-termino/<str:termino>/<int:id>/', views.editar_termino, name='editar_termino'),
    path('editar-termino/<str:termino>/<int:id>', views.editar_termino, name='editar_termino'),
    path('eliminar-termino/<int:id>/', views.eliminar_termino, name='eliminar_termino'),
    path('eliminar-termino/<int:id>', views.eliminar_termino, name='eliminar_termino'),
    path('agregar-definicion/', views.agregar_definicion, name='agregar_definicion'),
    path('agregar-definicion', views.agregar_definicion, name='agregar_definicion'),
    path('editar-definicion/<str:termino>/<int:id>/', views.editar_definicion, name='editar_definicion'),
    path('editar-definicion/<str:termino>/<int:id>', views.editar_definicion, name='editar_definicion'),
    path('eliminar-definicion/<str:letra>/<int:id>/', views.eliminar_definicion, name='eliminar_definicion'),
    path('eliminar-definicion/<str:letra>/<int:id>', views.eliminar_definicion, name='eliminar_definicion')
]