from django.contrib import admin

# Register your models here.

from app.models import usuario,apps,Membership

class AdminPag(admin.ModelAdmin):
    list_display = ["__unicode__", "nombre", "progreso", "pcUser","slug"]
    search_fields = ["nombre", "pcUser","slug"]
    list_editable = ["progreso","pcUser","slug"]
    list_filter = ["nombre"]
    class Meta:
        model = usuario

admin.site.register(usuario, AdminPag)

class AdminPag(admin.ModelAdmin):
    list_display = ["iduser", "nombre", "ruta"]

    class Meta:
        model = apps

admin.site.register(apps, AdminPag)

class AdminPag(admin.ModelAdmin):
    list_display = ["usuario", "apps", "conexion"]

    class Meta:
        model = Membership

admin.site.register(Membership, AdminPag)