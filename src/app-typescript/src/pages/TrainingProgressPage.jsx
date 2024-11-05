import React, { useState, useEffect } from 'react';
import ProgressBar from '../components/ProgressBar';
import Header from '../components/Header';
const TrainingProgressPage = () => {
    const [progress, setProgress] = useState(0);
    // Simula o progresso do treinamento do modelo
    useEffect(() => {
        const interval = setInterval(() => {
            setProgress((prev) => {
                if (prev < 100) {
                    return prev + 10;
                }
                else {
                    clearInterval(interval);
                    return 100;
                }
            });
        }, 1000);
    }, []);
    return (
      <div className="min-h-screen bg-gradient-to-b from-[#333641] to-[#282A32] flex flex-col items-center justify-center">
      <Header />
      <h1 className="text-3xl font-bold text-white text-center mt-8">Dados de Treinamento</h1>
      <div className="border-2 border-dashed border-gray-600 rounded-lg mx-auto mt-10 p-10 w-96 h-60 flex items-center justify-center">
        <p className="text-gray-400 text-center">O modelo está sendo treinado.</p>
      </div>
      <div className="w-11/12 mx-auto mt-10 flex flex-col items-center">
        <ProgressBar progress={progress} />
        <p className="text-center text-gray-400 mt-2">Processando...</p>
      </div>
      </div>
    );
};
export default TrainingProgressPage;
