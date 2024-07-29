from django.urls import path
from .views import (
    AsistenciaListCreate, AsistenciaDetail,
    EstudianteListCreate, EstudianteDetail,
    FaltaAsistenciaListCreate, FaltaAsistenciaDetail,
    FaltaPagoListCreate, FaltaPagoDetail,
    JustificacionListCreate, JustificacionDetail,
    PagoListCreate, PagoDetail,
    ServicioListCreate, ServicioDetail,
    UniversityListCreate, UniversityDetail
)

urlpatterns = [
    # Rutas para Asistencia
    path('asistencias/', AsistenciaListCreate.as_view(), name='asistencia-list-create'),
    path('asistencias/<int:pk>/', AsistenciaDetail.as_view(), name='asistencia-detail'),
    
    # Rutas para Estudiante
    path('estudiantes/', EstudianteListCreate.as_view(), name='estudiante-list-create'),
    path('estudiantes/<int:pk>/', EstudianteDetail.as_view(), name='estudiante-detail'),
    
    # Rutas para FaltaAsistencia
    path('faltas-asistencia/', FaltaAsistenciaListCreate.as_view(), name='falta-asistencia-list-create'),
    path('faltas-asistencia/<int:pk>/', FaltaAsistenciaDetail.as_view(), name='falta-asistencia-detail'),
    
    # Rutas para FaltaPago
    path('faltas-pago/', FaltaPagoListCreate.as_view(), name='falta-pago-list-create'),
    path('faltas-pago/<int:pk>/', FaltaPagoDetail.as_view(), name='falta-pago-detail'),
    
    # Rutas para Justificacion
    path('justificaciones/', JustificacionListCreate.as_view(), name='justificacion-list-create'),
    path('justificaciones/<int:pk>/', JustificacionDetail.as_view(), name='justificacion-detail'),
    
    # Rutas para Pago
    path('pagos/', PagoListCreate.as_view(), name='pago-list-create'),
    path('pagos/<int:pk>/', PagoDetail.as_view(), name='pago-detail'),
    
    # Rutas para Servicio
    path('servicios/', ServicioListCreate.as_view(), name='servicio-list-create'),
    path('servicios/<int:pk>/', ServicioDetail.as_view(), name='servicio-detail'),
    
    # Rutas para University
    path('universidades/', UniversityListCreate.as_view(), name='university-list-create'),
    path('universidades/<int:pk>/', UniversityDetail.as_view(), name='university-detail'),
]
