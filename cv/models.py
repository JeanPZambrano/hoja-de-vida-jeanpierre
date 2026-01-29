from django.db import models

# 1. PERFIL
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
        verbose_name_plural = "Perfil"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# 2. EXPERIENCIA
class Experiencia(models.Model):
    cargo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.cargo} en {self.empresa}"

# 3. EDUCACIÓN (MODIFICADO: Sin fecha y con descripción)
class Educacion(models.Model):
    titulo = models.CharField(max_length=100)
    institucion = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción corta")

    class Meta:
        verbose_name_plural = "Educación"

    def __str__(self):
        return self.titulo

# 4. PROYECTOS
class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    link = models.URLField(blank=True, null=True)
    imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True)

    def __str__(self):
        return self.titulo

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

    def __str__(self):
        return self.titulo

# 7. PRODUCTOS (GARAGE)
class Producto(models.Model):
    titulo = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.titulo

# 8. REFERENCIAS
class Referencia(models.Model):
    nombre = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} - {self.empresa}"