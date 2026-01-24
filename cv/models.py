from django.db import models

class Perfil (models.Model):
    nombre = models.CharField (max_length = 100)
    profesion = models.CharField (max_length = 100)
    descripcion = models.TextField ()
    email = models.EmailField ()
    telefono = models.CharField (max_length = 20)
    ubicacion = models.CharField (max_length = 100)
    linkedin = models.URLField (blank = True)
    github = models.URLField (blank = True)
    foto = models.ImageField (upload_to = 'perfil/', blank = True, null = True)

    def __str__(self):
        return self.nombre

class Educacion (models.Model):
    institucion = models.CharField (max_length = 150)
    titulo = models.CharField (max_length = 150)
    fecha_inicio = models.DateField ()
    fecha_fin = models.DateField (blank = True, null = True)
    descripcion = models.TextField (blank = True)

    def __str__(self):
        return f"{self.titulo} - {self.institucion}"

class Experiencia (models.Model):
    empresa = models.CharField (max_length = 150)
    cargo = models.CharField (max_length = 150)
    fecha_inicio = models.DateField ()
    fecha_fin = models.DateField (blank = True, null = True)
    descripcion = models.TextField ()

    def __str__(self):
        return f"{self.cargo} - {self.empresa}"

class Habilidad (models.Model):
    nombre = models.CharField (max_length = 100)
    nivel = models.IntegerField (help_text = "Nivel del 1 al 5")

    def __str__(self):
        return self.nombre

class Certificado(models.Model):
    perfil = models.ForeignKey(
        Perfil,
        on_delete=models.CASCADE,
        related_name="certificados"
    )
    titulo = models.CharField(max_length=200)
    institucion = models.CharField(max_length=200)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to="certificados/")

    def __str__(self):
        return self.titulo

class Proyecto(models.Model):
    perfil = models.ForeignKey(
        Perfil,
        on_delete=models.CASCADE,
        related_name="proyectos"
    )
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    tecnologias = models.CharField(max_length=300)
    github = models.URLField(blank=True, null=True)
    demo = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Referencia(models.Model):
    nombre = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.empresa}"