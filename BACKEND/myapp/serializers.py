from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Asistencia, Estudiante , FaltaAsistencia , FaltaPago , Justificacion , Pago, Servicio , University

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = '__all__'

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'

class FaltaAsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaltaAsistencia
        fields = '__all__'

class FaltaPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaltaPago
        fields = '__all__'

class JustificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Justificacion
        fields = '__all__'

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'