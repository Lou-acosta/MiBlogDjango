from django.contrib import admin
from django.urls import include, path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
    path('about/', views.about, name='about'),
]

