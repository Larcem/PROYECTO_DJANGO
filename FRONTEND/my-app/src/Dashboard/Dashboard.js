import './Dashboard.css';
import PagosList from './Pagos'; 
import Asistencia from './Asistencia';
import React, { useState } from 'react';
import Justificacion from './Justificacion'; 

function Dashboard() {
  const [menuOpen, setMenuOpen] = useState(true); 
  const [userMenuOpen, setUserMenuOpen] = useState(false);
  const [currentView, setCurrentView] = useState(''); 

  const toggleSidebar = () => {
    setMenuOpen(!menuOpen);
    setUserMenuOpen(false);
  };

  const toggleUserMenu = () => {
    setUserMenuOpen(!userMenuOpen); 
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
