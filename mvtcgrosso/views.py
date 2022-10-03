from unittest import loader
from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from datetime import datetime



from home.models import Familiar

def crear_familiar(request,nombre,apellido,edad):
    familia=Familiar(nombre=nombre,apellido=apellido,edad=edad,fechanac=datetime.now())
    familia.save()
    template= get_template('crearfamiliar.html')
    template_renderizado=template.render({'familia':familia})
    return HttpResponse(template_renderizado)

def ver_familiares(request):
    familiares=Familiar.objects.all()
    
    template= get_template('verfamiliares.html')
    template_renderizado=template.render({'familiares':familiares})
    return HttpResponse(template_renderizado)