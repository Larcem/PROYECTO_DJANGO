from django.urls import path
from .views import (
    PagoListCreate, PagoDetail,
    ServicioListCreate, ServicioDetail,
    FaltaPagoListCreate, FaltaPagoDetail,
    AsistenciaListCreate, AsistenciaDetail,
    EstudianteListCreate, EstudianteDetail,
    UniversityListCreate, UniversityDetail,
    JustificacionListCreate, JustificacionDetail,
    FaltaAsistenciaListCreate, FaltaAsistenciaDetail,
)

urlpatterns = [
    
    path('asistencias/', AsistenciaListCreate.as_view(), name='asistencia-list-create'),
    path('asistencias/<int:pk>/', AsistenciaDetail.as_view(), name='asistencia-detail'),
    
    path('estudiantes/', EstudianteListCreate.as_view(), name='estudiante-list-create'),
    path('estudiantes/<int:pk>/', EstudianteDetail.as_view(), name='estudiante-detail'),
    
    path('faltas-asistencia/', FaltaAsistenciaListCreate.as_view(), name='falta-asistencia-list-create'),
    path('faltas-asistencia/<int:pk>/', FaltaAsistenciaDetail.as_view(), name='falta-asistencia-detail'),
    
    path('faltas-pago/', FaltaPagoListCreate.as_view(), name='falta-pago-list-create'),
    path('faltas-pago/<int:pk>/', FaltaPagoDetail.as_view(), name='falta-pago-detail'),
    
    path('justificaciones/', JustificacionListCreate.as_view(), name='justificacion-list-create'),
    path('justificaciones/<int:pk>/', JustificacionDetail.as_view(), name='justificacion-detail'),
    
    path('pagos/', PagoListCreate.as_view(), name='pago-list-create'),
    path('pagos/<int:pk>/', PagoDetail.as_view(), name='pago-detail'),

    path('servicios/', ServicioListCreate.as_view(), name='servicio-list-create'),
    path('servicios/<int:pk>/', ServicioDetail.as_view(), name='servicio-detail'),
    
    path('universidades/', UniversityListCreate.as_view(), name='university-list-create'),
    path('universidades/<int:pk>/', UniversityDetail.as_view(), name='university-detail'),
]
