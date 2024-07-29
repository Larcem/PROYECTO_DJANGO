import React, { useEffect, useState } from 'react';
import { getAllPagos } from '../api/api'; 
import './Pagos.css'; 

const PagosList = () => {
  const [pagos, setPagos] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchPagos = async () => {
      try {
        const data = await getAllPagos();
        setPagos(data.data); 
      } catch (err) {
        setError(err.message);
      }
    };

    fetchPagos();
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
    return date.toLocaleString('es-ES', options); 
  };

  if (error) return <p>Error: {error}</p>;
  if (pagos.length === 0) return <p>No hay pagos disponibles.</p>;

  return (
    <ul className='Pagos_ul'>
      {pagos.map(pago => (
        <li key={pago.id_pago} className='Pagos_li'>
          {pago.estudiante} - {pago.monto} - {pago.status ? 'Activo' : 'Inactivo'} - {formatDate(pago.created)}
        </li>
      ))}
    </ul>
  );
};

export default PagosList;
