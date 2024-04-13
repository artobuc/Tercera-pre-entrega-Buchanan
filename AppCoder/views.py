from django.shortcuts import render
from AppCoder.models import Curso, Avatar
from AppCoder.models import Alumnos
from AppCoder.models import Profesores
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario , UserEditForm
from AppCoder.forms import Alumnos_formulario
from AppCoder.forms import Profesores_formulario
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.


def inicio(request):
    return render(request, "padre.html")


def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")

            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password=contra)

            if user is not None:

                login(request , user )
                login(request , user )
                avatares = Avatar.objects.filter(user=request.user.id)
                return render( request , "inicio.html" , {"url":avatares[0].imagen.url})
            else:

                return HttpResponse(f"Usuario no encontrado")
        else:

            return HttpResponse(f"FORM INCORRECTO {form}")
    form = AuthenticationForm()

    return render( request , "login.html" , {"form":form})




def register(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Usuario creado")

    else:
        form = UserCreationForm()
    return render(request , "registro.html" , {"form":form})


def editarPerfil(request):

    usuario = request.user

    if request.method == "POST":

        mi_formulario = UserEditForm(request.POST)

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data

            usuario.email = informacion["email"]

            password = informacion["password1"]

            usuario.set_password(password)

            usuario.save()

            return render(request , "inicio.html")

    else:

        miFormulario = UserEditForm(initial={"email":usuario.email})

    

    return render( request , "editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario})



def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


def ver_alumnos(request):
    alumnos = Alumnos.objects.all()
    dicc2 = {"alumnos": alumnos}
    plantilla2 = loader.get_template("alumnos.html")
    documento2 = plantilla2.render(dicc2)
    return HttpResponse(documento2)


def ver_profesores(request):
    profesores = Profesores.objects.all()
    dicc3 = {"profesores": profesores}
    plantilla3 = loader.get_template("profesores.html")
    documento3 = plantilla3.render(dicc3)
    return HttpResponse(documento3)


@login_required
def curso_formulario(request):
    if request.method == "POST":

        mi_formulario = Curso_formulario(request.POST)

        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            curso= Curso(nombre=request.POST["nombre"], camada=request.POST["camada"])
            curso.save()
            return render(request,"formulario.html")

    return render(request,"formulario.html")

@login_required
def alumnos_formulario(request):
    if request.method == "POST":

        mi_formulario = Alumnos_formulario(request.POST)

        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            alumnos= Alumnos(nombre=request.POST["nombre"], camada=request.POST["camada"])
            alumnos.save()
            return render(request,"formulario2.html")

    return render(request,"formulario2.html")

@login_required
def profesores_formulario(request):
    if request.method == "POST":

        mi_formulario = Profesores_formulario(request.POST)

        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            profesores= Profesores(nombre=request.POST["nombre"], camada=request.POST["camada"])
            profesores.save()
            return render(request,"formulario3.html")

    return render(request,"formulario3.html")


@login_required
def buscar_curso(request):
    return render(request,"buscar_curso.html")

@login_required
def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains= nombre)
        return render( request , "resultado_busqueda.html" , {"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")
    

@login_required
def elimina_curso(request , id ):
    curso = Curso.objects.get(id=id)
    curso.delete()

    curso = Curso.objects.all()

    return render(request , "cursos.html" , {"cursos":curso})

@login_required
def editar_curso(request , id):

    curso = Curso.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos["nombre"]
            curso.camada = datos["camada"]
            curso.save()

            curso = Curso.objects.all()

            return render(request , "cursos.html" , {"cursos":curso})


        
    else:
        mi_formulario = Curso_formulario(initial={"nombre":curso.nombre , "camada":curso.camada})
    
    return render( request , "editar_curso.html" , {"mi_formulario": mi_formulario , "curso":curso})

@login_required
def elimina_alumnos(request , id ):
    alumno = Alumnos.objects.get(id=id)
    alumno.delete()

    alumno = Alumnos.objects.all()

    return render(request , "alumnos.html" , {"alumno":alumno})

@login_required
def editar_alumnos(request , id):

    alumno = Alumnos.objects.get(id=id)

    if request.method == "POST":

        mi_formulario2 = Alumnos_formulario( request.POST )
        if mi_formulario2.is_valid():
            datos = mi_formulario2.cleaned_data
            alumno.nombre = datos["nombre"]
            alumno.camada = datos["camada"]
            alumno.save()

            alumno = Alumnos.objects.all()

            return render(request , "alumnos.html" , {"alumno":alumno})


        
    else:
        mi_formulario2 = Alumnos_formulario(initial={"nombre":alumno.nombre , "camada":alumno.camada})
    
    return render( request , "editar_alumnos.html" , {"mi_formulario2": mi_formulario2 , "alumno":alumno})

@login_required
def elimina_profesores(request , id ):
    profesor = Profesores.objects.get(id=id)
    profesor.delete()

    profesor = Profesores.objects.all()

    return render(request , "profesores.html" , {"profesor":profesor})

@login_required
def editar_profesores(request , id):

    profesor = Profesores.objects.get(id=id)

    if request.method == "POST":

        mi_formulario3 = Profesores_formulario( request.POST )
        if mi_formulario3.is_valid():
            datos = mi_formulario3.cleaned_data
            profesor.nombre = datos["nombre"]
            profesor.camada = datos["camada"]
            profesor.save()

            profesor = Profesores.objects.all()

            return render(request , "profesores.html" , {"profesor":profesor})


        
    else:
        mi_formulario3 = Profesores_formulario(initial={"nombre":profesor.nombre , "camada":profesor.camada})
    
    return render( request , "editar_profesores.html" , {"mi_formulario3": mi_formulario3 , "profesor":profesor})



