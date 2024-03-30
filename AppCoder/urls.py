from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="home"),
    path("ver_cursos", views.ver_cursos, name="cursos"),
    #path("alta_curso/<nombre>", views.alta_curso),
    path("alta_curso", views.curso_formulario, name="alta_curso"),
    path("buscar_curso", views.buscar_curso, name="buscar_curso"),
    path("ver_alumnos", views.ver_alumnos, name="alumnos"),
    path("alta_alumnos", views.alumnos_formulario, name="alta_alumnos"),
    path("ver_profesores", views.ver_profesores, name="profesores"),
    path("alta_profesores", views.profesores_formulario, name="alta_profesores"),
    path("buscar", views.buscar, name="buscar")

]