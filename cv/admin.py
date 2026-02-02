from django.contrib import admin
from .models import Perfil, Experiencia, Educacion, Proyecto, Certificado, Producto, Curso

# --- ESTO ES LO QUE CAMBIA EL TEXTO ---
# Al ponerlo aquí, nos aseguramos de que se aplique al cargar la app
admin.site.site_header = "Admin"             # Texto grande en la barra azul
admin.site.site_title = "Admin"              # Título en la pestaña del navegador
admin.site.index_title = "Panel de Control"  # Subtítulo (opcional)

# --- TUS REGISTROS ---
admin.site.register(Perfil)
admin.site.register(Experiencia)
admin.site.register(Educacion)
admin.site.register(Proyecto)
admin.site.register(Certificado)
admin.site.register(Producto)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'ver_pdf')
    search_fields = ('titulo', 'descripcion')
    
    def ver_pdf(self, obj):
        return "Sí" if obj.pdf_archivo else "No"
    ver_pdf.short_description = "¿Tiene PDF?"