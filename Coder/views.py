from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar
from django.template import loader


# Create your views here.

def familiares(request):                                                                                                                             
    familiar1 = Familiar(nombre="Gabriela",apellido="Ojeda",parentesco="hermana", edad = 33 , nacimiento = "2022-1-1" , email="email@etc")
    familiar2 = Familiar(nombre="Leonardo",apellido="Ojeda",parentesco="hermano", edad = 23 , nacimiento = "2022-1-1" , email="email2@etc")
    familiar3 = Familiar(nombre="Maria",apellido="Corsi",parentesco="abuela", edad = 90 , nacimiento = "2022-1-1" , email="404 not found lol")
    #familiar1.save()
    #familiar2.save()
    #familiar3.save()
    texto1= f"Nombre{familiar1.nombre},apellido{familiar1.apellido},parentesco{familiar1.parentesco},edad{familiar1.edad},fecha de nacimiento{familiar1.nacimiento},email{familiar1.email}"
    texto2= f"Nombre{familiar2.nombre},apellido{familiar2.apellido},parentesco{familiar2.parentesco},edad{familiar2.edad},fecha de nacimiento{familiar2.nacimiento},email{familiar2.email}"
    texto3= f"Nombre{familiar3.nombre},apellido{familiar3.apellido},parentesco{familiar3.parentesco},edad{familiar3.edad},fecha de nacimiento{familiar3.nacimiento},email{familiar3.email}"
    
    diccionario = {"texto1":texto1,"texto2":texto2,"texto3":texto3}
    plantilla = loader.get_template("plantilla.html")
    template = plantilla.render(diccionario)
    return HttpResponse(template)