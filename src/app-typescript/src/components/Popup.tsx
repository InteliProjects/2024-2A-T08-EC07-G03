import React from 'react';

interface PopupProps {
  isVisible: boolean;
  onClose: () => void;
  onConfirm: () => void;  
}

const Popup: React.FC<PopupProps> = ({ isVisible, onClose, onConfirm }) => {
  if (!isVisible) return null;

  return (
    <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
      <div className="bg-white rounded-lg p-8 shadow-lg max-w-sm w-full">
        <h2 className="text-gray-900 text-2xl mb-4 text-center">
          Para treinar o modelo, insira sua chave de autenticação
        </h2>
        <input
          type="text"
          placeholder="Insira sua chave"
          className="border border-gray-300 rounded-lg p-2 w-full text-center text-lg focus:outline-none focus:ring focus:border-blue-300"
        />
        <div className="mt-4 flex justify-end space-x-16">
          <button
            onClick={onClose}
            className="px-8 py-2 bg-gray-200 text-gray-800 rounded hover:bg-gray-300"
          >
            Fechar
          </button>
          <button
            onClick={onConfirm}
            className="px-6 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
          >
            Confirmar
          </button>
        </div>
      </div>
    </div>
  );
};

export default Popup;
