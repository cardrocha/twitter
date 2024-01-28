from .import views
from django.contrib import admin
from django.urls import path, include
from usuarios.views import cadastro


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('feeds/', include('feed.urls')),
    path('', cadastro),
    path('update_server/', views.update, name='update'),
]
