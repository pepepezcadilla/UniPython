from django.urls import path
from . import views

urlpatterns = [
    path('actors/', views.actor_list, name='actor_list'),
    path('actors/<int:actor_id>/', views.actor_detail, name='actor_detail'),
]
