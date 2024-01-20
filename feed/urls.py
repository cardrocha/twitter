from django.urls import path
from .import views

urlpatterns = [
  path('feed/', views.feed, name="feed"),
  path('logout/', views.logout, name="logout"),
  path('deletar_tweet/<int:id>', views.deletar_tweet, name="deletar_tweet"),
]