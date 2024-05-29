from django.urls import path
from AppCoder.views import curso, lista_cursos, inicio, cursos, profesores, estudiantes, entregables

urlpatterns = [
    path('nuevo-curso/<nombre>/<camada>', curso),
    path('lista-cursos/', lista_cursos),
    path('', inicio),
    path('cursos/', cursos),
    path('profesores', profesores),
    path('estudiantes/', estudiantes),
    path('entregables/', entregables),
]
