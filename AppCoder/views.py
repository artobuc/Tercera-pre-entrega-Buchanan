from django.shortcuts import render
from AppCoder.models import Curso
from AppCoder.models import Alumnos
from AppCoder.models import Profesores
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario
from AppCoder.forms import Alumnos_formulario
from AppCoder.forms import Profesores_formulario
# Create your views here.


def inicio(request):
    return render(request, "padre.html")





def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def ver_alumnos(request):
    cursos = Alumnos.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def ver_profesores(request):
    cursos = Profesores.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)



def curso_formulario(request):
    if request.method == "POST":

        mi_formulario = Curso_formulario(request.POST)

        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            curso= Curso(nombre=request.POST["nombre"], camada=request.POST["camada"])
            curso.save()
            return render(request,"formulario.html")

    return render(request,"formulario.html")

def alumnos_formulario(request):
    if request.method == "POST":

        mi_formulario = Alumnos_formulario(request.POST)

        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            alumnos= Alumnos(nombre=request.POST["nombre"], camada=request.POST["camada"])
            alumnos.save()
            return render(request,"formulario2.html")

    return render(request,"formulario2.html")

def profesores_formulario(request):
    if request.method == "POST":

        mi_formulario = Profesores_formulario(request.POST)

        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            profesores= Profesores(nombre=request.POST["nombre"], camada=request.POST["camada"])
            profesores.save()
            return render(request,"formulario3.html")

    return render(request,"formulario3.html")



def buscar_curso(request):
    return render(request,"buscar_curso.html")


def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains= nombre)
        return render( request , "resultado_busqueda.html" , {"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")
    

#alumnos

