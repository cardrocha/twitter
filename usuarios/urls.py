from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('profile_list/', views.profile_list, name="profile_list"),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('', views.cadastro_user, name="cadastro"),
    path('update_perfil/', views.update_perfil, name="update_perfil"),
    path('cadastro/', views.cadastro_user, name='cadastro_redirect'),
    path('delete_tweet/<int:id>', views.delete_tweet, name='delete_tweet')
]