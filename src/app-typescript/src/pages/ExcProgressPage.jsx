import React, { useState, useEffect } from 'react';
import BarExc from '../components/BarExc';
import Header from '../components/Header';
import { useNavigate, useLocation } from 'react-router-dom';
const ExcProgressPage = () => {
    const [progress, setProgress] = useState(0); // Estado do progresso visual
    const [isLoading, setIsLoading] = useState(true); // Estado para indicar se o carregamento ainda está em andamento
    const navigate = useNavigate();
    const location = useLocation();
    const { knr } = location.state || {}; // Obtém o KNR passado da página anterior
    // Simula o progresso visual do carregamento
    useEffect(() => {
        const interval = setInterval(() => {
            setProgress((prev) => {
                if (prev < 90) { // Simula o progresso até 90%
                    return prev + 10;
                }
                else {
                    clearInterval(interval);
                    return prev;
                }
            });
        }, 1000);
        return () => clearInterval(interval);
    }, []);
    // Faz a chamada da predição assim que o componente for montado
    useEffect(() => {
        const processPrediction = async () => {
            try {
                // Faz a chamada para a predição no servidor
                const response = await fetch('http://3.84.220.52:8000/api/model/predict', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ knr }),
                });
                console.log(response.body);
                if (response.ok) {
                    const data = await response.json();
                    console.log("Resultado da predição:", data);
                    const predictionStatus = data['prediction']['status'];
                    console.log("Status da predição:", predictionStatus);
                    // Predição concluída, definir o progresso como 100%
                    await new Promise(f => setTimeout(f, 5000)); // Simula um tempo de espera de 5 segundos
                    navigate('/excModel', { state: { result_atual: data['prediction']['status'], knr } });
                    setProgress(100);
                }
                else {
                    console.error('Erro na predição');
                }
            }
            catch (error) {
                console.error('Erro ao processar a predição:', error);
            }
            finally {
                setIsLoading(false); // Define o estado como carregamento concluído
            }
        };
        processPrediction();
    }, [knr, navigate]);
    return (<div className="min-h-screen bg-gradient-to-b from-[#333641] to-[#282A32]">
      <Header />
      <h1 className="text-6xl font-light text-white text-center mt-8 mb-24">Dados Para Análise</h1>
      <div className="font-sans flex flex-col items-center justify-center border-gray-500 border-2 border-dashed bg-gradient-to-b from-[#333641] to-[#2D3039] h-72 w-full max-w-lg mx-auto mt-10 bg-gray-800">
        <p className="text-gray-400">O modelo está sendo executado...</p>
      </div>
      <div className="w-72 mx-auto mt-20">
        <BarExc progress={progress}/>
        <p className="text-center text-gray-400 mt-2">Processando...</p>
      </div>
    </div>);
};
export default ExcProgressPage;
