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
    ...

##  Administración con Django
    Se muestran los pasos realizados para crear el Proyecto, la aplicación, creacion de modelos, migraciones y habilitación del panel de administración en Django.
    ...

##  Plantillas Bootstrap
    Se seleccionó la siguiente plantilla para el usuario final (No administrador).

    Demo online:
    URL: ...

    Se muestran las actividades realizadas para adecuación de plantillas, vistas, formularios en Django.
    ...

##  CRUD - Core Business - Clientes finales
    El núcleo de negocio del sistema de inscripciones tiene valor de aceptación para los cliente finales (alumnos) radica en realizar el proceso de inscripción propiamente, que empieza desde que:
    1. El alumno inicia sesión.
    2. El alumno selecciona el o los cursos donde desea realizar una inscripción.
    3. El alumno selecciona el grupo de laboatorio donde desea incribirse.
    4. El alumno puede tener la posibilidad de anular una incripción por varias razones: cambio de grupo, corregir error, etc.
    5. El alumno puede ver el consolidado de sus inscripciones.
    6. El alumno cierra sesión.

    Todas y cada una de estas pantallas debe funcionar en la plantilla bootstrap.
    A continuación se muestran las actividades realizadas para su construcción:
    ...

##  Servicios mediante una API RESTful
    Se ha creado una aplicación que pondra a disposición cierta información para ser consumida por otros clientes HTTP.
    1. GET : Con el método get se devolverá la lista de cursos, grupos y horarios establecidos para que el alumno sobre todo vea esta información en cualquier otro medio. En formato JSON. 
    2. POST : Con este método se enviara el código del alumno y se devolvera sus inscripciones. En formato JSON.
    
    Ejemplo: Prueba en Página web, aplicación móvil, PDF, etc.
    Se especifican los pasos para crear el servicio RestFul
    ...

##  Operaciones asíncronas AJAX
    Se propone el uso de AJAX para realizar la asignación de carga académica a los docentes que estan registrados. Esta operación la realizará el usuario operador encargado por el DAISI.
    Se muestran los pasos necesarios a realizar.
    ....

##  Investigación: Email, Upload.
    - Email: Se utilizará la funcionalidad del uso de envío de correos electrónicos cuando el proceso de inscripciones culmine y al profesor le llegue la lista de alumnos inscritos en sus grupos a cargo.
    - Upload: Se utilizará esta funcionalidad para subír, archivos CSV para importar y exportar información en el sistema.
    Se muestran los pasos realizados para su funcionamiento correcto.
    ...

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

[Debian]: https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white
[debian-site]: https://www.debian.org/index.es.html

[Git]: https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white
[git-site]: https://git-scm.com/

[GitHub]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
[github-site]: https://github.com/

[Vim]: https://img.shields.io/badge/VIM-%2311AB00.svg?style=for-the-badge&logo=vim&logoColor=white
[vim-site]: https://www.vim.org/

[Java]: https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=java&logoColor=white
[java-site]: https://docs.oracle.com/javase/tutorial/


[![Debian][Debian]][debian-site]
[![Git][Git]][git-site]
[![GitHub][GitHub]][github-site]
[![Vim][Vim]][vim-site]
[![Java][Java]][java-site]


[![License][license]][license-file]
[![Downloads][downloads]][releases]
[![Last Commit][last-commit]][releases]
