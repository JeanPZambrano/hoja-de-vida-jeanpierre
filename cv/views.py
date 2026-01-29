from django.shortcuts import render, get_object_or_404
from .models import Perfil, Experiencia, Educacion, Proyecto, Certificado, Producto, Reconocimiento, Referencia

def get_common_data():
    """Trae los datos básicos para el encabezado y el botón de perfiles"""
    perfiles = Perfil.objects.all()
    return {
        'perfil': perfiles.first(),
        'cantidad_perfiles': perfiles.count(),
    }

def home(request, pk=None):
    data = get_common_data()
    perfiles = Perfil.objects.all()
    
    if pk:
        data['perfil'] = get_object_or_404(Perfil, pk=pk)
    else:
        data['perfil'] = perfiles.first()

    # CORRECCIÓN: Eliminamos .order_by('-fecha_fin') de Educacion
    data['ultimas_experiencias'] = Experiencia.objects.all().order_by('-fecha_inicio')[:2]
    data['ultimos_proyectos'] = Proyecto.objects.all()[:2]
    data['ultima_educacion'] = Educacion.objects.all()[:2] 
    data['ultimos_productos'] = Producto.objects.filter(disponible=True)[:2]
    
    data['hide_sidebar'] = True 
    return render(request, 'cv/home.html', data)

def lista_perfiles(request):
    data = get_common_data()
    data['perfiles'] = Perfil.objects.all()
    data['hide_sidebar'] = True
    return render(request, 'cv/lista_perfiles.html', data)

def educacion(request):
    data = get_common_data()
    # CORRECCIÓN: Quitamos el ordenamiento por fecha inexistente
    data['educacion'] = Educacion.objects.all() 
    return render(request, 'cv/educacion.html', data)

def experiencia(request):
    data = get_common_data()
    data['experiencia'] = Experiencia.objects.all().order_by('-fecha_inicio')
    return render(request, 'cv/experiencia.html', data)

def proyectos(request):
    data = get_common_data()
    data['proyectos'] = Proyecto.objects.all()
    return render(request, 'cv/proyectos.html', data)

def certificados(request):
    data = get_common_data()
    data['reconocimientos'] = Reconocimiento.objects.all().order_by('-fecha')
    data['hide_sidebar'] = True 
    return render(request, 'cv/certificados.html', data)

def garage(request):
    data = get_common_data()
    data['productos'] = Producto.objects.all()
    data['hide_sidebar'] = True 
    return render(request, 'cv/garage.html', data)

def generar_cv(request):
    data = {
        'perfil': Perfil.objects.first(),
        'experiencia': Experiencia.objects.all().order_by('-fecha_inicio'),
        # CORRECCIÓN: Quitamos el ordenamiento aquí también
        'educacion': Educacion.objects.all(),
        'proyectos': Proyecto.objects.all(),
        'certificados': Certificado.objects.all(), 
        'reconocimientos': Reconocimiento.objects.all().order_by('-fecha'),
        'productos': Producto.objects.all(),
    }
    if request.GET:
        data.update({f"show_{k}": request.GET.get(k) == 'on' for k in ['perfil', 'experiencia', 'educacion', 'proyectos', 'certificados', 'garage']})
    else:
        data.update({f"show_{k}": True for k in ['perfil', 'experiencia', 'educacion', 'proyectos', 'certificados', 'garage']})
    return render(request, 'cv/cv_print.html', data)