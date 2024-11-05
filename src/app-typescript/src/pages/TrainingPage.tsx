import React from 'react';
import Header from '../components/Header';
import FileUpload from '../components/FileUpload';
import { useNavigate } from 'react-router-dom';
import FileUpload_Resultados from '../components/FileUpload_Resultados';
import FileUpload_Status from '../components/FileUpload_Status';
import FileUpload_Falhas from '../components/FileUpload_Falhas';

const Title = () => {
    return (<h1 className="text-6xl font-light text-white text-center mt-8 mb-24 font-sans">
      Dados de Treinamento:
    </h1>);
};
const ConfirmButton = () => {
    const navigate = useNavigate();
    const handleTrainClick = () => {
        navigate('/progress');
    };
    return (<div className="flex justify-center mt-6">
      <button onClick={handleTrainClick} className="px-12 py-1 mt-8 bg-white text-gray-900 rounded-lg hover:bg-gray-200 transition duration-200">
        Confirmar
      </button>
    </div>);
};
const TrainingPage = () => {
    return (<div className="min-h-screen bg-gradient-to-b from-[#333641] to-[#282A32] font-sans">
      <Header />
      <Title />
      <div className="flex justify-center gap-4 mt-8">
        <FileUpload_Resultados />
        <FileUpload_Status />
        <FileUpload_Falhas />
      </div>
      <ConfirmButton />
    </div>);
};
export default TrainingPage;