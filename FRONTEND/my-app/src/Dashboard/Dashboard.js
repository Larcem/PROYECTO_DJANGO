import React, { useState } from 'react';
import './Dashboard.css';
import Asistencia from './Asistencia'; // Asegúrate de que la ruta sea correcta
import PagosList from './Pagos'; // Asegúrate de que la ruta sea correcta
import Justificacion from './Justificacion'; // Asegúrate de que la ruta sea correcta

function Dashboard() {
  const [menuOpen, setMenuOpen] = useState(true); // Estado para el menú principal
  const [userMenuOpen, setUserMenuOpen] = useState(false); // Estado para el menú de usuario
  const [currentView, setCurrentView] = useState(''); // Estado para el componente actual

  const toggleSidebar = () => {
    setMenuOpen(!menuOpen);
    setUserMenuOpen(false); // Cierra el menú de usuario cuando se repliega el sidebar
  };

  const toggleUserMenu = () => {
    setUserMenuOpen(!userMenuOpen); // Alterna el estado del menú de usuario
  };

  const showAsistencia = () => {
    setCurrentView('asistencia');
  };

  const showPagos = () => {
    setCurrentView('pagos');
  };

  const showJustificacion = () => {
    setCurrentView('justificacion');
  };

  const renderView = () => {
    switch (currentView) {
      case 'asistencia':
        return <Asistencia />;
      case 'pagos':
        return <PagosList />;
      case 'justificacion':
        return <Justificacion />;
      default:
        return <div>Selecciona una opción del menú</div>;
    }
  };

  return (
    <div className="dashboard-container">
      <div className={`sidebar ${menuOpen ? 'open' : 'closed'}`}>
        <button className="user-info" onClick={toggleUserMenu}>
          Usuario
        </button>
        {!userMenuOpen && (
          <div className={`menu-buttons ${menuOpen ? '' : 'hidden'}`}>
            <button className="sidebar-button" onClick={showAsistencia}>
              Asistencia
            </button>
            <button className="sidebar-button" onClick={showPagos}>
              Pago
            </button>
            <button className="sidebar-button" onClick={showJustificacion}>
              Justificación inasistencia
            </button>
            <button className="sidebar-button_cerrar">Cerrar sesión</button>
          </div>
        )}
      </div>
      <div className="main-content">
        {renderView()}
      </div>
    </div>
  );
}

export { Dashboard };
