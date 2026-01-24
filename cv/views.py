from django.shortcuts import render
from .models import Perfil, Educacion, Experiencia, Habilidad, Referencia

def cv_view (request):
    perfil = Perfil.objects.first ()
    educaciones = Educacion.objects.all ()
    experiencias = Experiencia.objects.all ()
    habilidades = Habilidad.objects.all ()
    referencias = Referencia.objects.all()

    context = {
        'perfil': perfil,
        'educaciones': educaciones.all (),
        'experiencias': experiencias.all (),
        'habilidades': habilidades.all (),
        'certificados': perfil.certificados.all (),
        'proyectos': perfil.proyectos.all (),
        'referencias': referencias.all(), 
    }

    return render (request, 'cv/cv.html', context)

def home(request):
    perfil = Perfil.objects.first()
    return render(request, 'cv/home.html', {'perfil': perfil})