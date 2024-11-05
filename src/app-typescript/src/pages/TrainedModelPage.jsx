import React, { useState, useEffect } from "react";
import Header from "../components/Header";
import ConfirmationPopup from "../components/ConfirmationPopup";

const TrainedModelPage = () => {
  const [isPopupVisible, setPopupVisible] = useState(false);
  const [modelTrainingData, setModelTrainingData] = useState([]);

  useEffect(() => {
    fetchModelTrainingData();
  }, []);

  const fetchModelTrainingData = async () => {
    try {
      const response = await fetch(
        "http://3.84.220.52:8000/api/analise/model-training"
      );
      const data = await response.json();
      setModelTrainingData(data);
    } catch (error) {
      console.error("Error fetching model training data:", error);
    }
  };

  const handleOpenPopup = () => {
    setPopupVisible(true);
  };

  const handleClosePopup = () => {
    setPopupVisible(false);
  };

  const getLastModel = () => {
    if (modelTrainingData.length === 0) return null;
    return modelTrainingData[modelTrainingData.length - 1];
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-[#333641] to-[#282A32] text-white p-8">
      <Header />
      <div className="flex flex-col items-center justify-center">
        <h1 className="text-6xl font-light mt-8 mb-24">Modelo Treinado:</h1>

        <div className="w-full max-w-2xl mb-8 overflow-x-auto">
          <table className="w-full bg-gray-800 rounded-lg">
            <thead>
              <tr className="bg-gray-700">
                <th className="p-2 text-left">ID</th>
                <th className="p-2 text-left">Nome do Modelo</th>
                <th className="p-2 text-left">Precisão do Treinamento</th>
                <th className="p-2 text-left">Data</th>
              </tr>
            </thead>
            <tbody>
              {modelTrainingData.map((item) => (
                <tr key={item.id} className="border-t border-gray-700">
                  <td className="p-2">{item.id}</td>
                  <td className="p-2">{item.model_name}</td>
                  <td className="p-2">{item.training_accuracy}%</td>
                  <td className="p-2">
                    {new Date(item.date).toLocaleDateString()}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <div className="w-full max-w-2xl mb-6">
        <label className="block text-gray-400 mb-2 text-2xl">Modelo Atual:</label>
        <div className="w-full bg-gray-300 h-10 rounded-lg flex justify-center items-center">
          <span className="text-black">
            {getLastModel()?.training_accuracy || 'N/A'}
          </span>
        </div>
      </div>
      
      <div className="w-full max-w-2xl mb-4">
        <label className="block text-gray-400 mb-2 text-2xl">Modelo Anterior:</label>
        <div className="w-full bg-gray-300 h-10 rounded-lg flex justify-center items-center">
          <span className="text-black">{modelTrainingData.find(item => item.atual)?.training_accuracy || 'N/A'}%</span>
        </div>
      </div>

      <div className="w-full max-w-2xl mt-12 text-center">
        <p className="text-gray-400 text-2xl">Selecione qual modelo</p>
        <p className="text-gray-400 mb-12 text-2xl">você deseja utilizar:</p>
        <div className="flex justify-center space-x-4"></div>
          <button className="bg-gray-200 text-black px-12 py-1 mr-10 rounded-lg hover:bg-gray-300 transition" onClick={handleOpenPopup}>
            Atual
          </button>
          <button className="bg-gray-200 text-black px-12 py-1 rounded-lg hover:bg-gray-300 transition" onClick={handleOpenPopup}>
            Anterior
          </button>
        </div>

        {isPopupVisible && <ConfirmationPopup onClose={handleClosePopup} />}
      </div>
      </div>
  );
};

export default TrainedModelPage;
