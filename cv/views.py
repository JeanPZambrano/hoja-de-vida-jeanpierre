from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf import settings
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.cache import never_cache
import weasyprint 

# Importamos TODOS los modelos, incluido Curso
from .models import Perfil, Experiencia, Educacion, Proyecto, Certificado, Producto, Curso

def get_contexto_comun():
    return {
        'perfil': Perfil.objects.first(),
    }

# --- VISTAS NORMALES (WEB) ---

def home(request):
    context = get_contexto_comun()
    context['active_tab'] = 'inicio'
    context['hide_sidebar'] = True 
    
    # Resúmenes para la portada
    context['ultimos_proyectos'] = Proyecto.objects.all().order_by('-id')[:2]
    context['ultima_educacion'] = Educacion.objects.all().order_by('-fecha')[:2]
    context['ultima_experiencia'] = Experiencia.objects.all().order_by('-fecha_inicio')[:2]
    context['ultimos_certificados'] = Certificado.objects.all().order_by('-id')[:4]
    context['ultimos_productos'] = Producto.objects.filter(disponible=True)[:3]
    
    # Cursos en el inicio (3 más recientes)
    context['ultimos_cursos'] = Curso.objects.all().order_by('-fecha')[:3]
    
    return render(request, 'cv/home.html', context)

def experiencia(request):
    context = get_contexto_comun()
    context['active_tab'] = 'experiencia'
    context['experiencia'] = Experiencia.objects.all().order_by('-fecha_inicio')
    return render(request, 'cv/experiencia.html', context)

def educacion(request):
    context = get_contexto_comun()
    context['active_tab'] = 'educacion'
    context['productos_academicos'] = Educacion.objects.all().order_by('-fecha')
    return render(request, 'cv/educacion.html', context)

def proyectos(request):
    context = get_contexto_comun()
    context['active_tab'] = 'proyectos'
    context['proyectos'] = Proyecto.objects.all()
    return render(request, 'cv/proyectos.html', context)

def certificados(request):
    context = get_contexto_comun()
    context['active_tab'] = 'certificados'
    context['certificados'] = Certificado.objects.all()
    return render(request, 'cv/certificados.html', context)

def garage(request):
    context = get_contexto_comun()
    context['active_tab'] = 'garage'
    context['productos'] = Producto.objects.all()
    return render(request, 'cv/garage.html', context)

# Vista dedicada a Cursos
def cursos(request):
    context = get_contexto_comun()
    context['active_tab'] = 'cursos'
    context['cursos'] = Curso.objects.all().order_by('-fecha')
    # Usamos cursos_lista.html que extiende de base.html
    return render(request, 'cv/cursos_lista.html', context)

# --- VISTA GENERADOR DE PDF ---

@xframe_options_exempt 
@never_cache 
def descargar_cv_pdf(request):
    if request.method == 'POST':
        # Capturamos opciones (True si está marcado, False si no)
        opciones = {
            'incluir_perfil': request.POST.get('incluir_perfil') == 'on',
            'incluir_experiencia': request.POST.get('incluir_experiencia') == 'on',
            'incluir_educacion': request.POST.get('incluir_educacion') == 'on',
            'incluir_proyectos': request.POST.get('incluir_proyectos') == 'on',
            'incluir_academicos': request.POST.get('incluir_academicos') == 'on',
            'incluir_certificados': request.POST.get('incluir_certificados') == 'on',
            'incluir_cursos': request.POST.get('incluir_cursos') == 'on', # <--- IMPORTANTE
        }
        
        context = get_contexto_comun()
        context['opciones'] = opciones
        context['MEDIA_ROOT'] = settings.MEDIA_ROOT
        
        # Cargamos todos los datos (el template decide si mostrarlos u ocultarlos según 'opciones')
        context['experiencia'] = Experiencia.objects.all().order_by('-fecha_inicio')
        context['educacion'] = Educacion.objects.all().order_by('-fecha')
        context['proyectos'] = Proyecto.objects.all()
        context['certificados'] = Certificado.objects.all()
        context['cursos'] = Curso.objects.all().order_by('-fecha') 
        
        context['productos_academicos'] = context['educacion']

        html = render_to_string('cv/pdf_template.html', context)
        response = HttpResponse(content_type='application/pdf')
        
        accion = request.POST.get('action', 'download') 
        tipo_visualizacion = 'inline' if accion == 'preview' else 'attachment'
        
        response['Content-Disposition'] = f'{tipo_visualizacion}; filename="mi_cv.pdf"'
        
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        
        weasyprint.HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(response)
        return response
    
    return redirect('home')