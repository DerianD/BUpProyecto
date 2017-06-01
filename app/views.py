from django.shortcuts import render

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import usuario,apps,Membership
from system.multipleslug import MultiSlugMixin
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import get_object_or_404
from .forms import userModelForm
from django.db.models import Q
from django.shortcuts import render_to_response
# Create your views here.

def home(request):
    return render(request, 'index.html')

def info(request):
    return render(request, 'info.html')

def appinfo(request):
    return render(request, 'infoapp.html')

def userpag(request):
    us = Membership.objects.all()
    use = apps.objects.all()
    wasd = usuario.objects.all()
    template = "user.html"
    contexto= {"us":us,
                "use":use,
                "userr":wasd}
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


#########################
#Consultas y mas
class agregar_info(CreateView):
    model = usuario
    form_class = userModelForm
    success_url = "/login/"
   
   
    def get_context_data(self, *args, **kwargs):
        context = super(agregar_info, self).get_context_data(*args, **kwargs)
        context["submit_btn"]="Crear"
        return context

class actualizar(UpdateView):
    model = usuario
    form_class = userModelForm                                                            
    success_url = "/perfil/"

    def get_context_data(self, *args, **kwargs):
        context = super(actualizar, self).get_context_data(*args, **kwargs)
        context["submit_btn"]="Editar"
        return context

class usuarioslista(ListView):
    model = usuario

    def get_queryset(self, *args, **kwargs):
        qs = super(usuarioslista, self).get_queryset(**kwargs)
        bs = self.request.GET.get("q")
        if bs:
            qset = (
                Q(nombre__icontains=bs) |
                Q(edad__icontains=bs) |
                Q(progreso__icontains=bs)
            )
            qs = usuario.objects.filter(qset).distinct()
        
        print bs
        return qs