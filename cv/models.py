from django.db import models

# 1. PERFIL PERSONAL
class Perfil(models.Model):
    nombre = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    resumen = models.TextField(blank=True, null=True)
    ubicacion = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='perfil/', blank=True, null=True)
    cv_pdf = models.FileField(upload_to='cv_oficial/', blank=True, null=True, verbose_name="CV en PDF")

    ci = models.CharField(max_length=20, blank=True, null=True, verbose_name="Cédula / DNI")
    barrio = models.CharField(max_length=100, blank=True, null=True, verbose_name="Barrio / Sector")
    fecha_nacimiento = models.DateField(blank=True, null=True, verbose_name="Fecha de Nacimiento")

    def __str__(self):
        return self.nombre


# 2. EXPERIENCIA LABORAL
class Experiencia(models.Model):
    cargo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.cargo} en {self.empresa}"


# 3. EDUCACIÓN
class Educacion(models.Model):
    titulo = models.CharField(max_length=100)
    institucion = models.CharField(max_length=100)
    fecha_fin = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.titulo


# 4. PROYECTOS
class Proyecto(models.Model):
    titulo = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField()
    link = models.URLField(blank=True, null=True)
    imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True)

    def __str__(self):
        return self.titulo or "Proyecto"


# 5. CERTIFICADOS
class Certificado(models.Model):
    titulo = models.CharField(max_length=100)
    institucion = models.CharField(max_length=100)
    fecha = models.DateField(blank=True, null=True)
    archivo = models.FileField(upload_to='certificados/', blank=True, null=True)

    def __str__(self):
        return self.titulo


# 6. RECONOCIMIENTOS
class Reconocimiento(models.Model):
    titulo = models.CharField(max_length=100)
    institucion = models.CharField(max_length=100)
    fecha = models.DateField(blank=True, null=True)
    archivo = models.FileField(upload_to='reconocimientos/', blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo


# 7. PRODUCTOS
class Producto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    disponible = models.BooleanField(default=True, verbose_name="¿Está disponible?")

    def __str__(self):
        return self.titulo


# 8. REFERENCIAS
class Referencia(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.empresa}"
