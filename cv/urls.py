from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Ruta de Inicio (La que te faltaba)
    path('', views.home, name='home'),
    
    # Rutas de las secciones principales
    path('experiencia/', views.experiencia, name='experiencia'),
    path('educacion/', views.educacion, name='educacion'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('certificados/', views.certificados, name='certificados'),
    path('garage/', views.garage, name='garage'),
    
    # La ruta nueva para imprimir el CV
    path('generar-cv/', views.generar_cv, name='generar_cv'),
]

# Configuración obligatoria para ver imágenes y PDFs
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)