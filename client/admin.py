from django.contrib import admin
from .models import Registro  # 👈 importa el modelo

admin.site.register(Registro)  # 👈 regístralo