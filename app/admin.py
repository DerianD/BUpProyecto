from django.contrib import admin

# Register your models here.

from app.models import usuario

class AdminPag(admin.ModelAdmin):
    list_display = ["__unicode__", "nombre", "progreso", "pcUser","slug"]
    search_fields = ["nombre", "pcUser","slug"]
    list_editable = ["progreso","pcUser","slug"]
    list_filter = ["nombre"]
    class Meta:
        model = usuario

admin.site.register(usuario, AdminPag)