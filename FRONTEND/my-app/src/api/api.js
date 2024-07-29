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