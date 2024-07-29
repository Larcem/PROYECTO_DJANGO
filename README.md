<div align="center">
<table>
    <theader>
        <tr>
            <td style="width:25%;"><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:80%; height:auto"/></td>
            <td>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
                <span style="font-weight:bold;">DEPARTAMENTO ACADÉMICO DE INGENIERÍA DE SISTEMAS E INFORMÁTICA</span><br />
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </td>            
        </tr>
    </theader>
    <tbody>
        <tr>
        <td colspan="2"><span style="font-weight:bold;">Proyecto web</span>: Desarrollo de una aplicación web para Comedor Universitario</td>
        </tr>
        <tr>
        <td colspan="2"><span style="font-weight:bold;">Fecha</span>:  2024/07/28</td>
        </tr>
    </tbody>
</table>
</div>

<div align="center">
<span style="font-weight:bold;">PROYECTO WEB</span><br />
</div>


<table>
<theader>
<tr><th>INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
    <tr>
        <td>ASIGNATURA:</td><td>Programación Web 2</td>
    </tr>
    <tr>
        <td>SEMESTRE:</td><td>III</td>
    </tr>
    <tr>
        <td>FECHA INICIO:</td><td>21-Jul-2024</td><td>FECHA FIN:</td>
        <td>28-Jul-2024</td><td>DURACIÓN:</td><td>04 horas</td>
    </tr>
    <tr>
        <td colspan="3">DOCENTES:
        <ul>
        <li>Richart Smith Escobedo Quispe - rescobedoq@unsa.edu.pe</li>
        </ul>
        </td>
    </<tr>
</tdbody>
</table>

#   WebApp con Django

[![License][license]][license-file]
[![Downloads][downloads]][releases]
[![Last Commit][last-commit]][releases]

[![Debian][Debian]][debian-site]
[![Git][Git]][git-site]
[![GitHub][GitHub]][github-site]
[![Vim][Vim]][vim-site]
[![Java][Java]][java-site]

##  Tipo de Sistema
    Se trata de una aplicación web, que permita la visualización y notificación de información personal sobre el comedor universitario a los comensales.

##  Requisitos del sistema
    El sistema debe satisfacer los siguientes requisitos funcionales y no funcionales:

    - RQ01 : El sistema debe estar disponible en Internet a traves de una URL.
    - RQ02 : El sistema debe permitir el inicio/cierre de sesión.
    - RQ03 : El sistema debe permitir visualizar el estado de pagos y faltas de cada comensal.

##  Modelo de datos
    El modelo de datos esta conformado por las siguientes entidades.

    -   Curso : En esta entidad se almacena la información de los cursos o asignaturas que se imparten en una Escuela Profesional. Ejemplo: Programación Web 2, III semestre, 02 horas teóricas, 04 horas de laboratorio, etc..
    -   Profesor : En esta entidad se almacena los datos de los profesores que se responsabilizan del avance académico en la enseñanza de los temas planificados en cada curso. Ejemplo: Richart Escobedo, rescobedoq@unsa.edu.pe, Magister, etc.
    -   Asistencia: En esta entidad se almacena la información sobre la asistencia diaria a cada una de las comidas de cada usuario mediante una variable booleana
    -   Estudiante: Esta entidad recopila la información necesaria sobre el estudiante con relación al comedor universitario, variables como: asistencia, nombre, escuela, tipo de servicio requerido(Desayuno, Almuerzo o cena), sede de comedor, etc.
    -   FaltaAsistencia: En esta entidad se almacena información sobre la falta a una de las comidas requeridas por el usuario, marcando la fecha y comida de falta.
    -   FaltaPago: En esta entidad se guarda información sobre alguna falta de pago del usuario, se almacena fecha.
    -   Justificacion: Esta entidad guarda las posibles justficaciones brindadas por el usuario con relación a una falta de pago o asistencia.
    -   Pago: En esta entidad se almacenan los pagos realizados por cada usuario.
    -   Servicio: Esta entidad define el tipo de servicio que requiere el estudiante dentro de la semana.
    -   Universidad: Esta entidad guarda el nombre de la universidad y almacena el sistema en general.

##  Diccionario de datos

    A continuación el diccionario de datos.

| Asistencia | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| estudiante | -- | -- | -- | -- | -- |
| user | -- | -- | -- | -- | -- |
| id_asistencia | Numérico | No | Sí | Ninguno | ID de Asistencia |
| status | Booleano | No | No | false | Estatus de asistencia |
| created | Date | No | No | /// | Fecha de creación |
| modified | Date | No | No | /// | Fecha de modificación |

| Estudiante | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| id_Estudiante | Numérico | No | Sí | Ninguno | ID de Estudiante |
| id_user | Numérico | No | No | 1 | ID de Usuario |
| nombre | Cadena | No | No | Ninguno | Nombre del Estudiante |
| apellido | Cadena | No | No | Ninguno | Apellido del Estudiante |
| carrera | Cadena | No | No | Ninguno | Carrera del Estudiante |
| correo | Cadena | No | No | Ninguno | Correo del Estudiante |
| status | Booleano | No | No | false | Estatus del Estudiante |
| created | Fecha y Hora | No | No | /// | Fecha de creación |
| modified | Fecha y Hora | No | No | /// | Fecha de modificación |

| FaltaAsistencia | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| Asistencia | Relación | No | No | Ninguno | Asistencia relacionada |
| id_user | Relación | No | No | 1 | Universidad relacionada |
| id_FaltaAsistencia | Numérico | No | Sí | Ninguno | ID de Falta de Asistencia |
| fecha | Fecha y Hora | No | No | /// | Fecha de creación |
| status | Booleano | No | No | false | Estatus de la Falta de Asistencia |
| created | Fecha y Hora | No | No | /// | Fecha de creación |
| modified | Fecha y Hora | No | No | /// | Fecha de modificación |

| FaltaPago | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| pago | Relación | No | No | Ninguno | Pago relacionado |
| id_user | Relación | No | No | 1 | Universidad relacionada |
| semana | Numérico | No | No | 1 | Semana de la falta de pago |
| status | Booleano | No | No | false | Estatus de la falta de pago |
| created | Fecha y Hora | No | No | /// | Fecha de creación |
| modified | Fecha y Hora | No | No | /// | Fecha de modificación |
| id_falta_pago | Numérico | No | Sí | Ninguno | ID de la falta de pago |


| Justificacion | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| FaltaAsistencia | Relación | No | No | Ninguno | Falta de asistencia relacionada |
| id_user | Relación | No | No | 1 | Universidad relacionada |
| id_justificacion | Numérico | No | Sí | Ninguno | ID de la justificación |
| descripcion | Texto | No | No | Ninguno | Descripción de la justificación |
| fecha | Fecha y Hora | No | No | /// | Fecha de creación |
| status | Booleano | No | No | false | Estatus de la justificación |
| created | Fecha y Hora | No | No | /// | Fecha de creación |
| modified | Fecha y Hora | No | No | /// | Fecha de modificación |

| Pago | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| Estudiante | Relación | No | No | Ninguno | Estudiante relacionado |
| id_user | Relación | No | No | 1 | Universidad relacionada |
| id_pago | Numérico | No | Sí | Ninguno | ID del pago |
| semana | Numérico | No | No | 1 | Semana del pago |
| monto | Flotante | No | No | 0.0 | Monto del pago |
| status | Booleano | No | No | false | Estatus del pago |
| created | Fecha y Hora | No | No | /// | Fecha de creación |
| modified | Fecha y Hora | No | No | /// | Fecha de modificación |

| Servicio | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| id_pago | Relación | No | No | Ninguno | Pago relacionado |
| in_user | Relación | No | No | 1 | Universidad relacionada |
| id_servicio | Numérico | No | Sí | Ninguno | ID del servicio |
| tipo | Cadena | No | No | Ninguno | Tipo de servicio |
| status | Booleano | No | No | false | Estatus del servicio |
| fecha | Fecha y Hora | No | No | /// | Fecha de creación |
| modified | Fecha y Hora | No | No | /// | Fecha de modificación |

| Universidad | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| name | Cadena | No | No | Ninguno | Nombre de la universidad |
| acronym | Cadena | No | No | Ninguno | Acrónimo de la universidad |
| web_page | URL | No | No | Ninguno | Página web de la universidad |
| description | Texto | No | No | Ninguno | Descripción de la universidad |
| status | Booleano | No | No | true | Estatus de la universidad |
| created | Fecha y Hora | No | No | /// | Fecha de creación |
| modified | Fecha y Hora | No | No | /// | Fecha de modificación |
| user_created | Relación | Sí | No | Ninguno | Usuario que creó la universidad |
| user_modified | Relación | Sí | No | Ninguno | Usuario que modificó la universidad |
...

##  Diagrama Entidad-Relación
    En la siguiente imagen podemos apreciar el diagrama de Entidad-Relación:
![ER Diagram](erd.png)

##  BACKEND (DJango)
    A continuación se muestra el backend de nuestra aplicación:
    Clase serializer: Este código permite convertir objetos de modelo en datos que pueden ser        enviados a través de una API REST, lo que facilita la comunicación entre la aplicación y los     clientes que la utilizan.
```python
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Asistencia, Estudiante , FaltaAsistencia , FaltaPago , Justificacion , Pago, servicio , University

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
        model = servicio
        fields = '__all__'

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'
```
    Clase views.py: Este sección del proyecto define una serie de vistas que permiten crear, leer, actualizar y eliminar objetos de diferentes modelos en una aplicación Django que utiliza DRF.
```python
    from rest_framework import generics
from rest_framework import generics
from .models.Asistencia import Asistencia
from .models.Estudiante import Estudiante
from .models.FaltaAsistencia import FaltaAsistencia
from .models.FaltaPago import FaltaPago
from .models.Justificacion import Justificacion
from .models.Pago import Pago
from .models.servicio import servicio
from .models.University import University
from .serializers import AsistenciaSerializer, EstudianteSerializer, FaltaAsistenciaSerializer, FaltaPagoSerializer, JustificacionSerializer, PagoSerializer, ServicioSerializer, UniversitySerializer

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
    queryset = servicio.objects.all()
    serializer_class = ServicioSerializer

class ServicioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = servicio.objects.all()
    serializer_class = ServicioSerializer

# Vistas para el modelo University
class UniversityListCreate(generics.ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

class UniversityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
```
    Clase admin.py: Este código registra los modelos de la aplicación en la interfaz de administración de Django, permitiendo a los administradores crear, leer, actualizar y eliminar objetos de manera sencilla y visual. La interfaz de administración es una herramienta segura y útil para gestionar los datos de la aplicación. Los modelos registrados incluyen Estudiante, Pago, Servicio, FaltaPago, Asistencia, FaltaAsistencia, Justificación y Universidad.
    
```python
    from django.contrib import admin
    from .models.Estudiante import Estudiante
    from .models.Pago import Pago
    from .models.servicio import servicio
    from .models.FaltaPago import FaltaPago
    from .models.Asistencia import Asistencia
    from .models.FaltaAsistencia import FaltaAsistencia
    from .models.Justificacion import Justificacion
    from .models.University import University
    
    admin.site.register(Estudiante)
    admin.site.register(Pago)
    admin.site.register(FaltaPago)
    admin.site.register(servicio)
    admin.site.register(Asistencia)
    admin.site.register(FaltaAsistencia)
    admin.site.register(Justificacion)
    admin.site.register(University)
```
##  FrontEnd (REACT)
    A continuación tenemos la clase api.js que es fundamental en el FrontEnd: Este archivo de servicios API en React interactúa con una API para obtener, agregar, eliminar y actualizar datos de diferentes recursos. Utiliza Axios para realizar peticiones HTTP. Las funciones se organizan por recurso, como asistencias, estudiantes, faltas de asistencia, etc. Cada función realiza una petición HTTP específica para interactuar con la API. El archivo proporciona una capa de abstracción para interactuar con la API de manera segura y eficiente. Las funciones para obtener datos realizan peticiones GET a la API. Las funciones para agregar datos realizan peticiones POST a la API. Las funciones para eliminar datos realizan peticiones DELETE a la API. Las funciones para actualizar datos realizan peticiones PUT a la API. El archivo también incluye una función para fetch asistencias que utiliza la función fetch para obtener datos de asistencias.
```python
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api';

// Funciones para Asistencia
export const getAllAsistencias = () => {
    return axios.get(`${API_URL}/asistencias/`);
};

export const getAsistenciaById = (id) => {
    return axios.get(`${API_URL}/asistencias/${id}/`);
};

// Funciones para Estudiante
export const getAllEstudiantes = () => {
    return axios.get(`${API_URL}/estudiantes/`);
};

export const getEstudianteById = (id) => {
    return axios.get(`${API_URL}/estudiantes/${id}/`);
};

// Funciones para FaltaAsistencia
export const getAllFaltasAsistencia = () => {
    return axios.get(`${API_URL}/faltas-asistencia/`);
};

export const getFaltaAsistenciaById = (id) => {
    return axios.get(`${API_URL}/faltas-asistencia/${id}/`);
};

// Funciones para FaltaPago
export const getAllFaltasPago = () => {
    return axios.get(`${API_URL}/faltas-pago/`);
};

export const getFaltaPagoById = (id) => {
    return axios.get(`${API_URL}/faltas-pago/${id}/`);
};

// Funciones para Justificacion
export const getAllJustificaciones = () => {
    return axios.get(`${API_URL}/justificaciones/`);
};

export const getJustificacionById = (id) => {
    return axios.get(`${API_URL}/justificaciones/${id}/`);
};

// Funciones para Pago
export const getAllPagos = () => {
    return axios.get(`${API_URL}/pagos/`);
};

export const getPagoById = (id) => {
    return axios.get(`${API_URL}/pagos/${id}/`);
};

// Funciones para Servicio
export const getAllServicios = () => {
    return axios.get(`${API_URL}/servicios/`);
};

export const getServicioById = (id) => {
    return axios.get(`${API_URL}/servicios/${id}/`);
};

// Funciones para University
export const getAllUniversidades = () => {
    return axios.get(`${API_URL}/universidades/`);
};

export const getUniversityById = (id) => {
    return axios.get(`${API_URL}/universidades/${id}/`);
};

// Funciones para agregar datos
export const addAsistencia = (asistencia) => {
    return axios.post(`${API_URL}/asistencias/`, asistencia);
};

export const addEstudiante = (estudiante) => {
    return axios.post(`${API_URL}/estudiantes/`, estudiante);
};

export const addFaltaAsistencia = (faltaAsistencia) => {
    return axios.post(`${API_URL}/faltas-asistencia/`, faltaAsistencia);
};

export const addFaltaPago = (faltaPago) => {
    return axios.post(`${API_URL}/faltas-pago/`, faltaPago);
};

export const addJustificacion = (justificacion) => {
    return axios.post(`${API_URL}/justificaciones/`, justificacion);
};

export const addPago = (pago) => {
    return axios.post(`${API_URL}/pagos/`, pago);
};

export const addServicio = (servicio) => {
    return axios.post(`${API_URL}/servicios/`, servicio);
};

export const addUniversity = (university) => {
    return axios.post(`${API_URL}/universidades/`, university);
};

// Funciones para eliminar datos
export const deleteAsistencia = (id) => {
    return axios.delete(`${API_URL}/asistencias/${id}/`);
};

export const deleteEstudiante = (id) => {
    return axios.delete(`${API_URL}/estudiantes/${id}/`);
};

export const deleteFaltaAsistencia = (id) => {
    return axios.delete(`${API_URL}/faltas-asistencia/${id}/`);
};

export const deleteFaltaPago = (id) => {
    return axios.delete(`${API_URL}/faltas-pago/${id}/`);
};

export const deleteJustificacion = (id) => {
    return axios.delete(`${API_URL}/justificaciones/${id}/`);
};

export const deletePago = (id) => {
    return axios.delete(`${API_URL}/pagos/${id}/`);
};

export const deleteServicio = (id) => {
    return axios.delete(`${API_URL}/servicios/${id}/`);
};

export const deleteUniversity = (id) => {
    return axios.delete(`${API_URL}/universidades/${id}/`);
};

// Funciones para actualizar datos
export const updateAsistencia = (id, asistencia) => {
    return axios.put(`${API_URL}/asistencias/${id}/`, asistencia);
};

export const updateEstudiante = (id, estudiante) => {
    return axios.put(`${API_URL}/estudiantes/${id}/`, estudiante);
};

export const updateFaltaAsistencia = (id, faltaAsistencia) => {
    return axios.put(`${API_URL}/faltas-asistencia/${id}/`, faltaAsistencia);
};

export const updateFaltaPago = (id, faltaPago) => {
    return axios.put(`${API_URL}/faltas-pago/${id}/`, faltaPago);
};

export const updateJustificacion = (id, justificacion) => {
    return axios.put(`${API_URL}/justificaciones/${id}/`, justificacion);
};

export const updatePago = (id, pago) => {
    return axios.put(`${API_URL}/pagos/${id}/`, pago);
};

export const updateServicio = (id, servicio) => {
    return axios.put(`${API_URL}/servicios/${id}/`, servicio);
};

export const updateUniversity = (id, university) => {
    return axios.put(`${API_URL}/universidades/${id}/`, university);
};

export const fetchAsistencias = async () => {
    try {
      const response = await fetch(API_URL);
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error fetching asistencias:', error);
      throw error;
    }
  };
```

##  Serializer
    Este archivo define serializadores para modelos de Django utilizando rest_framework. Los serializadores convierten objetos de modelos en datos serializados para API. Se definen 9 serializadores para diferentes modelos, incluyendo User, Asistencia, Estudiante, etc. Cada serializador incluye todos los campos del modelo (__all__). Estos serializadores se utilizan en vistas de Django Rest Framework para devolver datos en formato JSON.
```python
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
```
##Funcionamiento

    1. El alumno inicia sesión.
    2. El alumno selecciona el o los cursos donde desea realizar una inscripción.
    3. El alumno selecciona el grupo de laboatorio donde desea incribirse.
    4. El alumno puede tener la posibilidad de anular una incripción por varias razones: cambio de grupo, corregir error, etc.
    5. El alumno puede ver el consolidado de sus inscripciones.
    6. El alumno cierra sesión.
Github del proyecto:

URL en Heroku:

URL Playlist YouTube.
Producción de un PlayList en Youtube explicando cada una de los requerimientos.
Video 01 - Sistema - Requisitos.
Video 02 - Modelo de datos - DD - DER.
etc…


## REFERENCIAS
-   

#

[license]: https://img.shields.io/github/license/rescobedoq/pw2?label=rescobedoq
[license-file]: https://github.com/rescobedoq/pw2/blob/main/LICENSE

[downloads]: https://img.shields.io/github/downloads/rescobedoq/pw2/total?label=Downloads
[releases]: https://github.com/rescobedoq/pw2/releases/

[last-commit]: https://img.shields.io/github/last-commit/rescobedoq/pw2?label=Last%20Commit

[Git]: https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white
[git-site]: https://git-scm.com/

[GitHub]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
[github-site]: https://github.com/

[Java]: https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=java&logoColor=white
[java-site]: https://docs.oracle.com/javase/tutorial/


[![Git][Git]][git-site]
[![GitHub][GitHub]][github-site]
[![Vim][Vim]][vim-site]
[![Java][Java]][java-site]


[![License][license]][license-file]
[![Downloads][downloads]][releases]
[![Last Commit][last-commit]][releases]
