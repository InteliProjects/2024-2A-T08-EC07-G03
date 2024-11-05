import React, { useState } from 'react';
import ConfirmationPopup from './ConfirmationPopup';

const OpenPop: React.FC = () => {
  const [isPopupVisible, setPopupVisible] = useState(false);

  const handleOpenPopup = () => {
    setPopupVisible(true);
  };

  const handleClosePopup = () => {
    setPopupVisible(false);
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-900">
      <button
        className="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600"
        onClick={handleOpenPopup}
      >
        Abrir Pop-up
      </button>

      {isPopupVisible && <ConfirmationPopup onClose={handleClosePopup} />}
    </div>
  );
};

export default OpenPop;
