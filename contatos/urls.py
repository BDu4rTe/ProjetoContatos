from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contato_id>', views.show, name='show'),
    path('busca/', views.busca, name='busca'),
]
