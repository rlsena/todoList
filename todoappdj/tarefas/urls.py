from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [ 
    path('',views.index,name='index'),
    path('delete/<id>',views.excluir_tarefa,name='delete'),
]