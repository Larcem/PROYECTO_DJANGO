from rest_framework import generics
from rest_framework import generics
from .models import Asistencia
from .models import Estudiante
from .models import FaltaAsistencia
from .models import FaltaPago
from .models import Justificacion
from .models import Pago
from .models import Servicio
from .models import University
from .serializers import AsistenciaSerializer, EstudianteSerializer, FaltaAsistenciaSerializer, FaltaPagoSerializer, JustificacionSerializer, PagoSerializer, ServicioSerializer, UniversitySerializer


# Vistas para el modelo Asistencia
class AsistenciaListCreate(generics.ListCreateAPIView):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer 

class AsistenciaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer

# Vistas para el modelo Estudiante
class EstudianteListCreate(generics.ListCreateAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class EstudianteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

# Vistas para el modelo FaltaAsistencia
class FaltaAsistenciaListCreate(generics.ListCreateAPIView):
    queryset = FaltaAsistencia.objects.all()
    serializer_class = FaltaAsistenciaSerializer

class FaltaAsistenciaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FaltaAsistencia.objects.all()
    serializer_class = FaltaAsistenciaSerializer

# Vistas para el modelo FaltaPago
class FaltaPagoListCreate(generics.ListCreateAPIView):
    queryset = FaltaPago.objects.all()
    serializer_class = FaltaPagoSerializer

class FaltaPagoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FaltaPago.objects.all()
    serializer_class = FaltaPagoSerializer

# Vistas para el modelo Justificacion
class JustificacionListCreate(generics.ListCreateAPIView):
    queryset = Justificacion.objects.all()
    serializer_class = JustificacionSerializer

class JustificacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Justificacion.objects.all()
    serializer_class = JustificacionSerializer

# Vistas para el modelo Pago
class PagoListCreate(generics.ListCreateAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

class PagoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

# Vistas para el modelo Servicio
class ServicioListCreate(generics.ListCreateAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class ServicioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

# Vistas para el modelo University
class UniversityListCreate(generics.ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

class UniversityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
