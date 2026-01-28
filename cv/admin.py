from django.contrib import admin
from .models import Perfil, Experiencia, Educacion, Proyecto, Certificado, Producto, Reconocimiento, Referencia

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni', 'telefono')

admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Experiencia)
admin.site.register(Educacion)
admin.site.register(Proyecto)
admin.site.register(Certificado)
admin.site.register(Producto)
admin.site.register(Reconocimiento)
admin.site.register(Referencia)