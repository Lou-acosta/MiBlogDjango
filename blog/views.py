from django.shortcuts import render
from .forms import AutorForm, CategoriaForm, PostForm
from .models import Post, Autor
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

def home(request):
    return render(request, 'home.html')

@login_required
def crear_autor(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "¡Autor creado exitosamente!")
    return render(request, 'crear_autor.html', {'form': form})

@login_required
def editar_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    form = AutorForm(request.POST or None, instance=autor)
    if form.is_valid():
        form.save()
        messages.success(request, "¡Autor editado exitosamente!")
    return render(request, 'editar_autor.html', {'form': form})

@login_required
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

@login_required
def buscar_post(request):
    query = request.GET.get('q', '')
    resultados = Post.objects.filter(titulo__icontains=query) if query else []
    return render(request, 'buscar_post.html', {'resultados': resultados, 'query': query})

def listar_posts(request):
    posts = Post.objects.all()  # Recupera todos los posts
    if not posts.exists():
        mensaje = "No hay páginas aún"
    else:
        mensaje = None
    return render(request, 'blog/listar_posts.html', {'posts': posts, 'mensaje': mensaje})

def listar_autores(request):
    autores = Autor.objects.all()  # Recupera todos los autores
    return render(request, 'listar_autores.html', {'autores': autores})

@login_required
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_posts')  # Redirige a la lista de posts después de guardar
    else:
        form = PostForm()
    return render(request, 'crear_post.html', {'form': form})

@login_required
def editar_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('listar_posts')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/editar_post.html', {'form': form, 'post': post})

@login_required
def eliminar_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('listar_posts')
    return render(request, 'blog/eliminar_post.html', {'post': post})

def detalle_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Busca el post o lanza un error 404 si no existe
    return render(request, 'detalle_post.html', {'post': post})

def about(request):
    return render(request, 'about.html')

def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':  # Si se envía el formulario
        form = UserCreationForm(request.POST)
        if form.is_valid():  # Validar la información
            form.save()  # Guardar el usuario en la base de datos
            return redirect('login')  # Redirigir al login
    else:  # Si no se envía el formulario, mostrarlo vacío
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def logout_view(request):
    logout(request)  # Cerrar sesión
    return redirect('home')  # Redirigir a la página principal

@login_required
def editar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Busca el post, si no existe lanza error 404
    if request.method == 'POST':  # Si se envió el formulario
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()  # Guarda los cambios en la base de datos
            return redirect('detalle_post', post_id=post.id)  # Redirige al detalle del post
    else:  # Si se accede a la vista sin enviar el formulario
        form = PostForm(instance=post)
    return render(request, 'editar_post.html', {'form': form, 'post': post})

@login_required
def eliminar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Busca el post
    if request.method == 'POST':  # Si se confirma la eliminación
        post.delete()  # Elimina el post de la base de datos
        messages.success(request, "El post fue eliminado exitosamente.")
        return redirect('listar_posts')  # Redirige al listado de posts
    return render(request, 'eliminar_post.html', {'post': post})

@login_required
def profile_view(request):
    perfil = request.user.perfil
    return render(request, 'accounts/profile.html', {'perfil': perfil})