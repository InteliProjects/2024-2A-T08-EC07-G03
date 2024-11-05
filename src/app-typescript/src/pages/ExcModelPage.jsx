import React, { useState } from 'react';
import Header from '../components/Header';
import { useLocation } from 'react-router-dom';

const ExcModelPage = () => {
    const [isPopupVisible, setPopupVisible] = useState(false);
    const location = useLocation();
    const { result_atual, knr} = location.state || {};
    console.log(result_atual);

    const handleOpenPopup = () => {
        setPopupVisible(true);
    };

    const handleClosePopup = () => {
        setPopupVisible(false);
    };

    return (
        <div className="min-h-screen bg-gradient-to-b from-[#333641] to-[#282A32] text-white p-8">
            <Header />
            <div className="flex flex-col items-center justify-center">
                <h1 className="text-4xl font-light mb-24 mt-8">Modelo Executado:</h1>

                <div className="w-full shadow-2xl max-w-2xl h-32 bg-[#2F323C] justify-center">
                    <div className="text-white text-lg mb-2 mt-4 text-center">
                        Resultado da Predição:
                    </div>
                    <div className="text-white text-1xl text-center opacity-75">
                        KNR executado: {knr}
                    </div>
                </div>
                <div className="w-full max-w-2xl mb-4 mt-24">
                    <div className={`w-full shadow-2xl max-w-2xl h-32 flex flex-col items-center justify-center ${ result_atual === 'Tem falha' ? 'bg-red-500' : 'bg-green-500'}`}>
                    <label className="block font-black text-white opacity-75 mt-4">Resultado:</label>
                    <span className="text-white opacity-75 mt-2">
                        {result_atual === 'Tem falha' ? 'Tem falha' : 'Não tem falha'}
                    </span>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ExcModelPage;
