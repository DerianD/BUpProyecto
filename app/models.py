from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

############################
# Base de datos - tablas

class usuario(models.Model):
    nombre = models.CharField(max_length = 100)
    progreso = models.CharField(max_length = 100)
    edad = models.CharField(max_length = 100)
    slug = models.SlugField(blank=True, unique=True)
    pcUser = models.CharField(max_length = 100)
    def __unicode__(self):
        return self.nombre

class apps(models.Model):
    iduser = models.CharField(max_length = 100)
    ident= models.DecimalField(max_digits=8, decimal_places=0, null=True, blank=True)
    nombre = models.CharField(max_length = 100)
    ruta = models.CharField(max_length = 100)
    
    def __unicode__(self):
        return self.iduser

class Membership(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    apps = models.ForeignKey(apps, on_delete=models.CASCADE)
    conexion = models.CharField(max_length = 100)
    ultimaconexion = models.CharField(max_length = 100)
    

#########################
# Funciones - metodos
def create_slug(instance, nuevo_slug=None):
    slug = slugify(instance.nombre)
    if nuevo_slug is not None:
        slug = nuevo_slug

    qs = usuario.objects.filter(slug=slug)
    existe = qs.exists()
    if existe:
        nuevo_slug = "%s-%s" %(slug, qs.last().id)
        return create_slug(instance, nuevo_slug=nuevo_slug)

    return slug

def producto_pre_save_reciever(sender, instance, *args, **kwargs):
    print sender
    print instance

    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(producto_pre_save_reciever, sender=usuario)

