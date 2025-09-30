from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('recetas/', views.lista_recetas, name='lista_recetas'),
    path('receta/<int:id>/', views.detalle_receta, name='detalle_receta'),
    path('contacto/', views.contacto, name='contacto'),
    path('confirmacion/', views.confirmacion, name='confirmacion'),
]