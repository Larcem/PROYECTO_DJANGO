from django.db import models
from django.contrib.auth.models import User


class University(models.Model):
    name = models.CharField(max_length=100)
    acronym = models.CharField(max_length=50)
    web_page = models.URLField()
    description = models.TextField()
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user_created = models.ForeignKey(User, related_name='universities_created', on_delete=models.SET_NULL, null=True, blank=True)
    user_modified = models.ForeignKey(User, related_name='universities_modified', on_delete=models.SET_NULL, null=True, blank=True)
    
class Estudiante(models.Model):
    id_Estudiante = models.BigAutoField(primary_key=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True, blank=True)  # Permitir nulos
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    carrera = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    created = models.DateTimeField(editable=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Asistencia(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    user = models.ForeignKey(University, on_delete=models.CASCADE)
    id_asistencia = models.BigAutoField(primary_key=True)
    status = models.BooleanField(default=False)
    created = models.DateTimeField(editable=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Estudiante: {self.estudiante.nombre}, Status: {'Activo' if self.status else 'Inactivo'}, Creado: {self.created.strftime('%Y-%m-%d %H:%M:%S')}"

    
class FaltaAsistencia (models.Model):
    Asistencia =models.ForeignKey( Asistencia, on_delete=models.CASCADE)
    id_user=models.ForeignKey(University, on_delete=models.CASCADE, default=1)
    id_FaltaAsistencia = models.BigAutoField(primary_key=True)
    fecha = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    status =models.BooleanField(default=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    
class Pago (models.Model):
    Estudiante =models.ForeignKey( Estudiante, on_delete=models.CASCADE)
    id_user = models.ForeignKey(University, on_delete=models.CASCADE, default=1)
    id_pago = models.BigAutoField(primary_key=True)
    semana=models.IntegerField(default=1)
    monto=models.FloatField(default=0.0)
    status =models.BooleanField(default=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)

class FaltaPago (models.Model):
    pago =models.ForeignKey( Pago, on_delete=models.CASCADE)
    id_user=models.ForeignKey(University, on_delete=models.CASCADE, default=1)
    semana=models.IntegerField(default=1)
    status =models.BooleanField(default=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    id_falta_pago = models.BigAutoField(primary_key=True)
    
class Justificacion (models.Model):
    FaltaAsistencia =models.ForeignKey( FaltaAsistencia, on_delete=models.CASCADE)
    id_user=models.ForeignKey(University, on_delete=models.CASCADE, default=1)
    id_justificacion = models.BigAutoField(primary_key=True)
    descripcion=models.TextField()
    fecha = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    status =models.BooleanField(default=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    

    
class Servicio(models.Model):
    id_pago=models.ForeignKey(Pago , on_delete=models.CASCADE)
    in_user=models.ForeignKey(University, on_delete=models.CASCADE, default=1)
    id_servicio = models.BigAutoField(primary_key=True)
    tipo=models.CharField(max_length=100)
    status =models.BooleanField(default=False)
    fecha = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    status =models.BooleanField(default=False)
    


    
    


