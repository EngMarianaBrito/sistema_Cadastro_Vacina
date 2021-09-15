from django.contrib import admin

from .models import *

admin.site.register(Paciente)
admin.site.register(Enfermeiro)
admin.site.register(Vacinas)
admin.site.register(Estado)
admin.site.register(Locais)
admin.site.register(Cidade)
