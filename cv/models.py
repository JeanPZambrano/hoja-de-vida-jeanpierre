from django.db import models
from django.core.exceptions import ValidationError

class Perfil(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=10, verbose_name="Cédula/DNI", null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    sector = models.CharField(max_length=100, verbose_name="Barrio/Sector", null=True, blank=True)
    resumen = models.TextField()
    foto = models.ImageField(upload_to='perfil/', null=True, blank=True)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfil (Información Personal)"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Experiencia(models.Model):
    cargo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencia Laboral"

    def __str__(self):
        return f"{self.cargo} en {self.empresa}"

    def clean(self):
        super().clean()
        if self.fecha_inicio and self.fecha_fin:
            if self.fecha_inicio > self.fecha_fin:
                raise ValidationError("⛔ Error: La fecha de inicio no puede ser posterior a la fecha de fin.")

class Educacion(models.Model):
    titulo = models.CharField(max_length=100)
    institucion = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción corta")
    fecha = models.DateField(null=True, blank=True, verbose_name="Fecha de Finalización")

    class Meta:
        verbose_name = "Producto Académico"
        verbose_name_plural = "Productos Académicos"

    def __str__(self):
        return self.titulo

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=150, blank=True, null=True)
    descripcion = models.TextField()
    fecha = models.DateField(null=True, blank=True, verbose_name="Fecha de Realización")
    tecnologias = models.CharField(max_length=200, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True)

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos (Portafolio)"

    def __str__(self):
        return self.titulo

class Certificado(models.Model):
    titulo = models.CharField(max_length=100)
    institucion = models.CharField(max_length=100)
    fecha = models.DateField(blank=True, null=True)
    archivo = models.FileField(upload_to='certificados/', blank=True, null=True)

    class Meta:
        verbose_name = "Certificado"
        verbose_name_plural = "Certificados"

    def __str__(self):
        return self.titulo

# En models.py, busca la clase Producto y agrégale esto:

class Producto(models.Model):
    # ... (tus campos existentes) ...
    ESTADOS = [
        ('Nuevo', 'Nuevo / Sellado'),
        ('Como Nuevo', 'Como Nuevo (10/10)'),
        ('Buen Estado', 'Usado - Buen Estado'),
        ('Detalles', 'Usado - Con detalles estéticos'),
        ('Reparar', 'Para piezas / A reparar'),
    ]

    titulo = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=50, choices=ESTADOS, default='Buen Estado', verbose_name="Condición")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción detallada")
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    class Meta:
        verbose_name = "Producto de Venta"
        verbose_name_plural = "Garage (Ventas)"

    def __str__(self):
        return self.titulo

    # --- AGREGAR ESTA VALIDACIÓN ---
    def clean(self):
        super().clean()
        # Validar que el precio no sea negativo
        if self.precio < 0:
            raise ValidationError("⛔ Error: El precio no puede ser negativo (ej. -10). Por favor coloca 0 o un número positivo.")

# --- NUEVO MODELO CURSO ---
# En tu archivo models.py

class Curso(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título del Curso")
    descripcion = models.TextField(verbose_name="Descripción")
    fecha = models.DateField(verbose_name="Fecha de realización")
    
    pdf_archivo = models.FileField(upload_to='cursos/pdfs/', verbose_name="PDF del Curso")
    
    # --- CAMBIO AQUÍ: Agregamos null=True y blank=True ---
    vista_previa = models.ImageField(upload_to='cursos/previews/', verbose_name="Imagen de Vista Previa", null=True, blank=True)
    
    archivo_extra = models.FileField(upload_to='cursos/extras/', blank=True, null=True, verbose_name="Archivo Extra")

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['-fecha']

    def __str__(self):
        return self.titulo