from django.urls import path
from home.views import home, listado_de_calas

urlpatterns = [
    path('', home, name= 'home'),
    path('calas/', listado_de_calas, name= 'listar_calas'),

]
