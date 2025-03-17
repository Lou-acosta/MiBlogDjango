from django.shortcuts import render
from .forms import AutorForm, CategoriaForm, PostForm
from .models import Post, Autor
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect

def home(request):
    return render(request, 'home.html')

def crear_autor(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "¡Autor creado exitosamente!")
    return render(request, 'crear_autor.html', {'form': form})

def editar_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    form = AutorForm(request.POST or None, instance=autor)
    if form.is_valid():
        form.save()
        messages.success(request, "¡Autor editado exitosamente!")
    return render(request, 'editar_autor.html', {'form': form})

def eliminar_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    if request.method == 'POST':
        autor.delete()
        messages.success(request, "¡Autor eliminado exitosamente!")
        return redirect('home')  # Redirigir a la página principal
    return render(request, 'confirmar_eliminacion.html', {'autor': autor})

def crear_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'crear_categoria.html', {'form': form})

def buscar_post(request):
    query = request.GET.get('q', '')
    resultados = Post.objects.filter(titulo__icontains=query) if query else []
    return render(request, 'buscar_post.html', {'resultados': resultados, 'query': query})

def listar_posts(request):
    posts = Post.objects.all()  # Recupera todos los posts
    return render(request, 'listar_posts.html', {'posts': posts})

def listar_autores(request):
    autores = Autor.objects.all()  # Recupera todos los autores
    return render(request, 'listar_autores.html', {'autores': autores})

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_posts')  # Redirige a la lista de posts después de guardar
    else:
        form = PostForm()
    return render(request, 'crear_post.html', {'form': form})

def detalle_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Busca el post o lanza un error 404 si no existe
    return render(request, 'detalle_post.html', {'post': post})