from django.contrib import admin
from .models import Alumno
from .models import Reserva
from .models import Laboratorio

# Register your models here.
admin.site.register(Alumno)
admin.site.register(Reserva)
admin.site.register(Laboratorio)