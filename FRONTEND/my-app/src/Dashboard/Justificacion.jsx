// src/components/Justificacion.jsx
import React, { useState } from 'react';
import { addJustificacion } from '../api/api'; // Asegúrate de que la ruta sea correcta
import './Justificacion.css'; // Asegúrate de crear este archivo CSS

const Justificacion = () => {
  const [faltaAsistencia, setFaltaAsistencia] = useState('');
  const [descripcion, setDescripcion] = useState('');
  const [status, setStatus] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Datos para enviar
    const justificacionData = {
      FaltaAsistencia: faltaAsistencia,
      id_user: 1, // Aquí deberías establecer el ID del usuario de acuerdo a tu lógica de autenticación
      descripcion,
      status,
    };

    try {
      await addJustificacion(justificacionData);
      setSuccess('Justificación añadida con éxito');
      setFaltaAsistencia('');
      setDescripcion('');
      setStatus(false);
    } catch (err) {
      setError('Error al añadir la justificación');
    }
  };

  return (
    <div className="justificacion-container">
      <h2>Agregar Justificación</h2>
      {error && <p className="error">{error}</p>}
      {success && <p className="success">{success}</p>}
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="faltaAsistencia">Falta de Asistencia:</label>
          <input
            type="number"
            id="faltaAsistencia"
            value={faltaAsistencia}
            onChange={(e) => setFaltaAsistencia(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="descripcion">Descripción:</label>
          <textarea
            id="descripcion"
            value={descripcion}
            onChange={(e) => setDescripcion(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="status">Estado:</label>
          <input
            type="checkbox"
            id="status"
            checked={status}
            onChange={(e) => setStatus(e.target.checked)}
          />
        </div>
        <button type="submit">Enviar</button>
      </form>
    </div>
  );
};

export default Justificacion;
