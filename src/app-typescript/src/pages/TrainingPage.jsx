import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import FileUpload_Resultados from '../components/FileUpload_Resultados';
import FileUpload_Status from '../components/FileUpload_Status';
import FileUpload_Falhas from '../components/FileUpload_Falhas';
import Header from '../components/Header';

// Componente de título
const Title = () => {
    return (<h1 className="text-6xl font-light text-white text-center mt-8 mb-24 font-sans">
      Dados de Treinamento:
    </h1>);
};



const ConfirmButton = ({ resultados, falhas, status }) => {
  const navigate = useNavigate();

  const handleTrainClick = async () => {
      console.log('Botão confirmar clicado');

      // Verificar se os arrays foram inicializados corretamente
      if (!resultados || !falhas || !status) {
          console.error('Os arquivos não foram selecionados corretamente.');
          return;
      }

      // Verificar se os arquivos foram selecionados
      if (resultados.length === 0 || falhas.length === 0 || status.length === 0) {
          console.warn('Todos os arquivos precisam ser selecionados.');
          return;
      }

      const formData = new FormData();

      // Adicionando os arquivos ao FormData
      resultados.forEach((file) => {
          formData.append("resultados", file);
      });
      falhas.forEach((file) => {
          formData.append("falhas", file);
      });
      status.forEach((file) => {
          formData.append("status", file);
      });

      formData.append("save_new_model", "true");

      // Exibindo os dados no console para verificar
      console.log('FormData antes de enviar:', formData);

      try {
          const response = await fetch('http://127.0.0.1:8000/api/model/retrain', {
              method: 'POST',
              body: formData
          });

          if (response.ok) {
              const data = await response.json();
              console.log('Sucesso:', data);
              navigate('/progress'); // Navegar para a página de progresso após o sucesso
          } else {
              const errorData = await response.json();
              console.error('Erro na resposta do servidor:', errorData.detail);
          }
      } catch (error) {
          console.error('Erro ao enviar os arquivos:', error);
      }
  };

  return (
      <div className="flex justify-center mt-6">
          <button onClick={handleTrainClick} className="px-12 py-1 mt-8 bg-white text-gray-900 rounded-lg hover:bg-gray-200 transition duration-200">
              Confirmar
          </button>
      </div>
  );
};

const TrainingPage = () => {
  // Inicializando arrays vazios
  const [resultados, setResultados] = useState([]);
  const [falhas, setFalhas] = useState([]);
  const [status, setStatus] = useState([]);

  console.log('Renderizou o componente TrainingPage');

  return (
      <div className="min-h-screen bg-gradient-to-b from-[#333641] to-[#282A32] font-sans">
          <Header />
          <Title />
          <div className="flex justify-center gap-4 mt-8">
              <FileUpload_Resultados setFiles={setResultados} />
              <FileUpload_Falhas setFiles={setFalhas} />
              <FileUpload_Status setFiles={setStatus} />
          </div>
          <ConfirmButton resultados={resultados} falhas={falhas} status={status} />
      </div>
  );
};

export default TrainingPage;
