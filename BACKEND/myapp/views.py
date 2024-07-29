from .models import Pago
from .models import Servicio
from .models import FaltaPago
from .models import Asistencia
from .models import Estudiante
from .models import University
from .models import Justificacion
from rest_framework import generics
from rest_framework import generics
from .models import FaltaAsistencia
from .serializers import AsistenciaSerializer, EstudianteSerializer, FaltaAsistenciaSerializer, FaltaPagoSerializer, JustificacionSerializer, PagoSerializer, ServicioSerializer, UniversitySerializer


class AsistenciaListCreate(generics.ListCreateAPIView):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer 

class AsistenciaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer

class EstudianteListCreate(generics.ListCreateAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class EstudianteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class FaltaAsistenciaListCreate(generics.ListCreateAPIView):
    queryset = FaltaAsistencia.objects.all()
    serializer_class = FaltaAsistenciaSerializer

class FaltaAsistenciaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FaltaAsistencia.objects.all()
    serializer_class = FaltaAsistenciaSerializer

class FaltaPagoListCreate(generics.ListCreateAPIView):
    queryset = FaltaPago.objects.all()
    serializer_class = FaltaPagoSerializer

class FaltaPagoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FaltaPago.objects.all()
    serializer_class = FaltaPagoSerializer

class JustificacionListCreate(generics.ListCreateAPIView):
    queryset = Justificacion.objects.all()
    serializer_class = JustificacionSerializer

class JustificacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Justificacion.objects.all()
    serializer_class = JustificacionSerializer

class PagoListCreate(generics.ListCreateAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

class PagoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

class ServicioListCreate(generics.ListCreateAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class ServicioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class UniversityListCreate(generics.ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

class UniversityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
