from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

# Create your views here.
def curso(req, nombre, camada):
    nuevo_curso = Curso(nombre=nombre,camada=camada)
    nuevo_curso.save()
    return HttpResponse(f"El curso {nuevo_curso.nombre} fue creado con el numero {nuevo_curso.camada}")

def lista_cursos(req):
    lista = Curso.objects.all()
    return render(req, "lista_cursos.html", {"lista_cursos": lista}) 