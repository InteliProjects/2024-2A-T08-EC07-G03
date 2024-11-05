import React from 'react';
import Header from '../components/Header';
import FileUpload from '../components/FileUpload';
import { useNavigate } from 'react-router-dom';
const Title = () => {
    return (<h1 className="text-6xl font-light text-white text-center mt-8 mb-24 font-sans">
      Dados para Análise:
    </h1>);
};
const KNRInput = () => {
    return (<div className="flex flex-col items-center mt-8">
      <input type="text" placeholder="Digite seu KNR" className="w-full max-w-lg px-4 py-2 border border-white rounded-lg bg-transparent text-white placeholder-white focus:outline-none focus:ring-2 focus:ring-white font-light" id='krn_input'/>
    </div>);
};
const ConfirmButton = () => {
    const navigate = useNavigate();
    const handleTrainClick = async () => {
        try {
            const knr = document.getElementById('krn_input').value;
            console.log(knr);
            navigate('/excProgress', { state: { knr } });
        }
        catch (error) {
            console.log("Erro na requisição de predição", error);
        }
    };
    return (<div className="flex justify-center mt-6">
      <button onClick={handleTrainClick} className="px-12 py-1 mt-8 bg-white text-gray-900 rounded-lg hover:bg-gray-200 transition duration-200">
        Confirmar
      </button>
    </div>);
};
const ExcPage = () => {
    return (<div className="min-h-screen bg-gradient-to-b from-[#333641] to-[#282A32] font-sans">
      <Header />
      <Title />
      <FileUpload />
      <p className="text-gray-400 text-center mt-8">ou</p>
      <KNRInput />
      <ConfirmButton />
    </div>);
};
export default ExcPage;
