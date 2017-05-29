from django.shortcuts import render

from django.views.generic.detail import DetailView
from .models import usuario,apps,Membership
from system.multipleslug import MultiSlugMixin
from django.shortcuts import get_object_or_404
# Create your views here.

def home(request):
    return render(request, 'index.html')

def info(request):
    return render(request, 'info.html')

def appinfo(request):
    return render(request, 'infoapp.html')

def userpag(request):
    us = Membership.objects.all()
    template = "user.html"
    contexto= {"us":us}
    return render(request, template, contexto)


class usuarioDetailView(MultiSlugMixin, DetailView):
    model = usuario

def detalle(request, object_id=None):
    #Logico de negocio alias hechizo
    user = get_object_or_404(usuario, id=object_id)
    app = get_object_or_404(apps, id=object_id)
    mem = get_object_or_404(Membership, id=object_id)
    m = "productos nuevo"
    template = "pruevas.html"
    contexto= {"user":user,
           "apps": app,
           "mem": mem }
    return render(request, template, contexto)
