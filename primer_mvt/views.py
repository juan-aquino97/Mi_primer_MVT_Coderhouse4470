from django.http import HttpResponse

from django.template import Template, Context

from datetime import date

from django.template import loader

from datos_familia.models import Familiares


def listado_familia(request):
    
    familiares = Familiares.objects.all()

    datos = {"familiares": familiares, }

    plantilla = loader.get_template("template1.html")

    documento = plantilla.render(datos)
    
    return HttpResponse(documento)