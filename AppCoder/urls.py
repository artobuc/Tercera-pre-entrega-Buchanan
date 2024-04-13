from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicio, name="home"),
    path("ver_cursos", views.ver_cursos, name="cursos"),
    #path("alta_curso/<nombre>", views.alta_curso),
    path("alta_curso", views.curso_formulario, name="alta_curso"),
    path("buscar_curso", views.buscar_curso, name="buscar_curso"),
    path("elimina_curso/<int:id>" , views.elimina_curso , name="elimina_curso"),
    path("editar_curso/<int:id>" , views.editar_curso , name="editar_curso"),
    path("ver_alumnos", views.ver_alumnos, name="alumnos"),
    path("alta_alumnos", views.alumnos_formulario, name="alta_alumnos"),
    path("elimina_alumnos/<int:id>" , views.elimina_alumnos, name="elimina_alumnos"),
    path("editar_alumnos/<int:id>" , views.editar_alumnos , name="editar_alumnos"),
    path("ver_profesores", views.ver_profesores, name="profesores"),
    path("alta_profesores", views.profesores_formulario, name="alta_profesores"),
    path("elimina_profesores/<int:id>" , views.elimina_profesores, name="elimina_profesores"),
    path("editar_profesores/<int:id>" , views.editar_profesores , name="editar_profesores"),
    path("buscar", views.buscar, name="buscar"),
    path("login", views.login_request , name="Login"),
    path("register", views.register , name="Register"),
    path("logout" , LogoutView.as_view(template_name="logout.html") , name="Logout"),
    path("editarPerfil" , views.editarPerfil , name="EditarPerfil")
    


]