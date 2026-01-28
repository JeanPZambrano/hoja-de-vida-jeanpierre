from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('perfil/<int:pk>/', views.home, name='perfil_detalle'), # Para ver cada perfil completo
    path('perfiles/', views.lista_perfiles, name='lista_perfiles'),
    path('experiencia/', views.experiencia, name='experiencia'),
    path('educacion/', views.educacion, name='educacion'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('certificados/', views.certificados, name='certificados'), # <-- ESTA FALTABA
    path('garage/', views.garage, name='garage'),
    path('generar-cv/', views.generar_cv, name='generar_cv'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)