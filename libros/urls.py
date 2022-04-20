from os import path

from . import views

urlpatterns = [
 path('', views.index, name='index'), # Página home
 path('libros/', views.libro_list, name='libros'), # Listado de libros
 path('libros/create/', views.libro_create, name='libro_create'), # Formulario para crear nuevo libro
 path('libros/<int:id>/', views.libro_detail, name='libro_detail'), # Detalle de un libro
 path('libros/<int:id>/update/', views.libro_update, name='libro_update'), # Formulario paraactualizar un libro existente
 path('libros/<int:id>/delete/', views.libro_delete, name='libro_delete'), # Borrar un libro
]