from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página principal
    path('crear_autor/', views.crear_autor, name='crear_autor'),  # Crear autor
    path('listar_autores/', views.listar_autores, name='listar_autores'),  # Lista de autores
    path('editar_autor/<int:autor_id>/', views.editar_autor, name='editar_autor'),  # Editar autor
    path('eliminar_autor/<int:autor_id>/', views.eliminar_autor, name='eliminar_autor'),  # Eliminar autor
    path('buscar_post/', views.buscar_post, name='buscar_post'),
    path('listar_post/', views.listar_posts, name='listar_posts'),
    path('crear_post/', views.crear_post_view, name='crear_post'),
    path('posts/editar/<int:post_id>/', views.editar_post, name='editar_post'),
    path('posts/eliminar/<int:post_id>/', views.eliminar_post, name='eliminar_post'),
    path('post/<int:id>/', views.detalle_post_view, name='detalle_post'),
]

