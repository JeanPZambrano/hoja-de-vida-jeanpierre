from django.shortcuts import render
from .models import Perfil, Experiencia, Educacion, Proyecto, Certificado, Producto, Reconocimiento

def get_common_data():
    return {
        'perfil': Perfil.objects.first(),
    }

def home(request):
    data = get_common_data()
    
    # 1. Traemos datos para los resúmenes (Dashboard)
    data['ultimas_experiencias'] = Experiencia.objects.all().order_by('-fecha_inicio')[:2]
    data['ultimos_proyectos'] = Proyecto.objects.all()[:2]
    data['ultima_educacion'] = Educacion.objects.all().order_by('-fecha_fin')[:2]
    data['ultimos_productos'] = Producto.objects.filter(disponible=True)[:2]
    
    # 2. ESTA LÍNEA ES CLAVE: Oculta la barra lateral izquierda solo en Inicio
    data['hide_sidebar'] = True 
    
    return render(request, 'cv/home.html', data)

def experiencia(request):
    data = get_common_data()
    data['experiencia'] = Experiencia.objects.all().order_by('-fecha_inicio')
    return render(request, 'cv/experiencia.html', data)

def educacion(request):
    data = get_common_data()
    data['educacion'] = Educacion.objects.all().order_by('-fecha_fin')
    return render(request, 'cv/educacion.html', data)

def proyectos(request):
    data = get_common_data()
    data['proyectos'] = Proyecto.objects.all()
    return render(request, 'cv/proyectos.html', data)

def certificados(request):
    data = get_common_data()
    data['reconocimientos'] = Reconocimiento.objects.all().order_by('-fecha')
    
    # ESTA LÍNEA ES LA CLAVE: Oculta la barra lateral
    data['hide_sidebar'] = True 
    
    return render(request, 'cv/certificados.html', data)

def garage(request):
    data = get_common_data()
    data['productos'] = Producto.objects.all()
    
    # ESTA LÍNEA ES LA MAGIA: Oculta la barra lateral solo en esta página
    data['hide_sidebar'] = True 
    
    return render(request, 'cv/garage.html', data)
# --- AQUÍ ESTÁ LA MODIFICACIÓN CON DIAGNÓSTICO ---
def reconocimientos(request):
    data = get_common_data()
    
    # 1. Buscamos los datos
    lista = Reconocimiento.objects.all().order_by('-fecha')
    
    # 2. IMPRIMIMOS EN LA TERMINAL PARA VER QUÉ PASA
    print("========================================")
    print("¡HOLA! ESTOY ENTRANDO A LA VISTA DE RECONOCIMIENTOS")
    print(f"CANTIDAD ENCONTRADA: {lista.count()}")
    for item in lista:
        print(f" - Archivo encontrado: {item.titulo} | URL: {item.archivo}")
    print("========================================")
    
    # 3. Guardamos en el diccionario
    data['reconocimientos'] = lista
    
    return render(request, 'cv/reconocimientos.html', data)

# En cv/views.py (al final del archivo)

def generar_cv(request):
    # 1. Cargamos TODOS los datos de la base de datos
    data = {
        'perfil': Perfil.objects.first(),
        'experiencia': Experiencia.objects.all().order_by('-fecha_inicio'),
        'educacion': Educacion.objects.all().order_by('-fecha_fin'),
        'proyectos': Proyecto.objects.all(),
        # Unimos certificados y reconocimientos para que salgan juntos si se piden
        'certificados': Certificado.objects.all(), 
        'reconocimientos': Reconocimiento.objects.all().order_by('-fecha'),
        'productos': Producto.objects.all(),
    }

    # 2. Verificamos qué casillas marcó el usuario en el menú
    # Si no marca nada (entra directo), mostramos todo por defecto
    if request.GET:
        data['show_perfil'] = request.GET.get('perfil') == 'on'
        data['show_experiencia'] = request.GET.get('experiencia') == 'on'
        data['show_educacion'] = request.GET.get('educacion') == 'on'
        data['show_proyectos'] = request.GET.get('proyectos') == 'on'
        data['show_certificados'] = request.GET.get('certificados') == 'on'
        data['show_garage'] = request.GET.get('garage') == 'on'
    else:
        # Si entra sin parámetros, mostrar todo
        data.update({k: True for k in ['show_perfil', 'show_experiencia', 'show_educacion', 'show_proyectos', 'show_certificados', 'show_garage']})

    return render(request, 'cv/cv_print.html', data)