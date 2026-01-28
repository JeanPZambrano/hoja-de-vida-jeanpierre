from django.shortcuts import render, get_object_or_404
from .models import Perfil, Experiencia, Educacion, Proyecto, Certificado, Producto, Reconocimiento

def get_common_data():
    perfiles = Perfil.objects.all()
    return {
        'cantidad_perfiles': perfiles.count(),
    }

def home(request, pk=None):
    data = get_common_data()
    perfiles = Perfil.objects.all()
    
    # Si picaste en una tarjeta, cargamos ese ID. Si no, el primero.
    if pk:
        data['perfil'] = get_object_or_404(Perfil, pk=pk)
    else:
        data['perfil'] = perfiles.first()

    data['ultimas_experiencias'] = Experiencia.objects.all().order_by('-fecha_inicio')[:2]
    data['ultimos_proyectos'] = Proyecto.objects.all()[:2]
    data['ultima_educacion'] = Educacion.objects.all().order_by('-fecha_fin')[:2]
    data['ultimos_productos'] = Producto.objects.filter(disponible=True)[:2]
    data['hide_sidebar'] = True 
    return render(request, 'cv/home.html', data)

def lista_perfiles(request):
    data = get_common_data()
    data['perfiles'] = Perfil.objects.all()
    data['hide_sidebar'] = True
    return render(request, 'cv/lista_perfiles.html', data)

# Asegúrate de que todas estas funciones existan con estos nombres
def experiencia(request):
    data = get_common_data()
    data['perfil'] = Perfil.objects.first()
    data['experiencia'] = Experiencia.objects.all().order_by('-fecha_inicio')
    return render(request, 'cv/experiencia.html', data)

def educacion(request):
    data = get_common_data()
    data['perfil'] = Perfil.objects.first()
    data['educacion'] = Educacion.objects.all().order_by('-fecha_fin')
    return render(request, 'cv/educacion.html', data)

def proyectos(request):
    data = get_common_data()
    data['perfil'] = Perfil.objects.first()
    data['proyectos'] = Proyecto.objects.all()
    return render(request, 'cv/proyectos.html', data)

def certificados(request):
    data = get_common_data()
    data['perfil'] = Perfil.objects.first()
    data['reconocimientos'] = Reconocimiento.objects.all().order_by('-fecha')
    data['hide_sidebar'] = True 
    return render(request, 'cv/certificados.html', data)

def garage(request):
    data = get_common_data()
    data['perfil'] = Perfil.objects.first()
    data['productos'] = Producto.objects.all()
    data['hide_sidebar'] = True 
    return render(request, 'cv/garage.html', data)

def generar_cv(request):
    data = {'perfil': Perfil.objects.first()} # ... resto de la lógica que ya tienes
    return render(request, 'cv/cv_print.html', data)