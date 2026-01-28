from django.contrib import admin
from .models import Perfil, Experiencia, Educacion, Proyecto, Certificado, Producto, Reconocimiento, Referencia # <--- Agrega Referencia aquí

# ... tus otros registros ...

admin.site.register(Referencia) # <--- Agrega esta línea al final

admin.site.register(Perfil)
admin.site.register(Experiencia)
admin.site.register(Educacion)
admin.site.register(Proyecto)
admin.site.register(Certificado)
admin.site.register(Producto)

# --- ¡ESTA ES LA LÍNEA QUE TE FALTA! ---
admin.site.register(Reconocimiento)