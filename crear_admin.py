import os
import django
from django.contrib.auth import get_user_model

# IMPORTANTE: Usamos 'config.settings' porque así aparece en tu manage.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

User = get_user_model()
USERNAME = 'admin_render'
EMAIL = 'jeanpierrezambranodatos@gmail.com'
PASSWORD = 'ContrasenaSegura123'

if not User.objects.filter(username=USERNAME).exists():
    print(f"Creando superusuario {USERNAME}...")
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
    print("¡Superusuario creado exitosamente!")
else:
    print(f"El usuario {USERNAME} ya existe.")