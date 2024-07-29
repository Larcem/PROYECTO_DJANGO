// src/components/AsistenciasList.js
import React, { useEffect, useState } from 'react';
import { getAllAsistencias, getEstudianteById } from '../api/api'; // Asegúrate de que la ruta sea correcta
import './Asistencia.css'; // Importa el CSS correspondiente

const AsistenciasList = () => {
  const [asistencias, setAsistencias] = useState([]);
  const [error, setError] = useState(null);
  const [estudiantes, setEstudiantes] = useState({}); // Almacena datos del estudiante por ID

  useEffect(() => {
    const fetchAsistencias = async () => {
      try {
        const data = await getAllAsistencias();
        const asistenciasData = data["data"];
        setAsistencias(asistenciasData);

        // Obtén los estudiantes correspondientes
        const estudiantesPromises = asistenciasData.map(asistencia =>
          getEstudianteById(asistencia.estudiante).then(estudianteData => ({
            id: asistencia.estudiante,
            nombre: estudianteData.data.nombre,
          }))
        );
        
        // Espera a que todas las promesas se resuelvan
        const estudiantesArray = await Promise.all(estudiantesPromises);
        
        // Crea un objeto de estudiantes con ID como clave
        const estudiantesMap = estudiantesArray.reduce((acc, estudiante) => {
          acc[estudiante.id] = estudiante.nombre;
          return acc;
        }, {});

        setEstudiantes(estudiantesMap);
      } catch (err) {
        setError(err.message);
      }
    };

    fetchAsistencias();
  }, []);
  const formatDate = (isoString) => {
    const date = new Date(isoString);
    const options = {
      year: 'numeric',
      month: '2-digit',
      day: '2-digit',
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit',
      hour12: false,
    };
    return date.toLocaleString('es-ES', options); // Puedes ajustar el locale según tus necesidades
  };
  if (error) return <p>Error: {error}</p>;
  if (asistencias.length === 0) return <p>No hay asistencias disponibles.</p>;

  return (
    <ul className='Asistencia_ul'>
      {asistencias.map(asistencia => (
        <li key={asistencia.id_asistencia} className='Asistencia_li'>
          {estudiantes[asistencia.estudiante] || 'Cargando nombre...'} - {asistencia.status ? 'Activo' : 'Inactivo'} - {formatDate(asistencia.created)}
        </li>
      ))}
    </ul>
  );
};

export default AsistenciasList;
