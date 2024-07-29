from django.contrib import admin

from .models import Estudiante 
from .models import Pago
from .models import Servicio
from .models import FaltaPago
from .models import Asistencia
from .models import FaltaAsistencia
from .models import Justificacion
from .models import University

admin.site.register(Estudiante)
admin.site.register(Pago)
admin.site.register(FaltaPago)
admin.site.register(Servicio)
admin.site.register(Asistencia)
admin.site.register(FaltaAsistencia)
admin.site.register(Justificacion)
admin.site.register(University)

