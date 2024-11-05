import React from 'react';
import { useNavigate } from 'react-router-dom';
const ConfirmationPopup = ({ onClose }) => {
    const navigate = useNavigate();
    const handleConfirm = () => {
        // Redireciona para a tela de modelo treinado
        navigate('/exc');
    };
    return (<div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
      <div className="bg-gradient-to-b from-gray-800 to-gray-900 p-8 rounded-xl shadow-lg text-center">
        <h2 className="text-white text-xl mb-8">Tem certeza que deseja utilizar esse modelo?</h2>
        <div className="flex justify-around">
          <button className="bg-green-500 text-white px-4 py-2 rounded-md hover:bg-green-600" onClick={handleConfirm}>
            Sim
          </button>
          <button className="bg-red-500 text-white px-4 py-2 rounded-md hover:bg-red-600" onClick={onClose}>
            Não
          </button>
        </div>
      </div>
    </div>);
};
export default ConfirmationPopup;
