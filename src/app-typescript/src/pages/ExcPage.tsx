import React from 'react';
import Header from '../components/Header';
import FileUpload1 from '../components/FileUpload';
import { useNavigate } from 'react-router-dom';


const predictKNR = async (knr: string) => {
  const response = await fetch('http://3.84.220.52:8000/api/model/predict', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ knr }),
  });

  if (!response.ok) {
    throw new Error('Erro na predição');
  }

  return response.json();
};


const uploadCSV = async (file: File) => {
  const formData = new FormData();
  formData.append('file', file);

  const response = await fetch('http://3.84.220.52:8000/predict_batch', {
    method: 'POST',
    body: formData,
  });

  if (!response.ok) {
    throw new Error('Erro no upload de CSV');
  }

  return response.json();
};


const Title: React.FC = () => {
  return (
    <h1 className="text-4xl font-light text-white text-center mt-16 font-sans">
      Dados para Análise:
    </h1>
  );
};


const KNRInput: React.FC = () => {
  return (
    <div className="flex flex-col items-center mt-6">
      <input 
        type="text"
        placeholder="Digite seu KNR"
        className="w-full max-w-lg px-4 py-2 border border-gray-500 rounded-lg bg-transparent text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-white font-light"
        id='krn_input'
      />
    </div>
  );
};


const ConfirmButton: React.FC = () => {
  const navigate = useNavigate();

  const handleTrainClick = async () => {
    try {
      const knr = (document.getElementById('krn_input') as HTMLInputElement).value;
      if (knr) {

        const result = await predictKNR(knr);
        console.log(result);

        
        navigate('/excProgress', { state: { knr, result } });
      }
    } catch (error) {
      console.log("Erro na requisição de predição", error);
    }
  };

  return (
    <div className="flex justify-center mt-6">
      <button onClick={handleTrainClick} className="px-8 py-2 bg-white text-gray-900 rounded-lg hover:bg-gray-200 transition duration-200">
        Confirmar
      </button>
    </div>
  );
};


const FileUpload: React.FC = () => {
  const navigate = useNavigate();

  const handleFileChange = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      try {
        const result = await uploadCSV(file);
        console.log(result);

        navigate('/excProgress', { state: { result } });
      } catch (error) {
        console.log("Erro no upload de arquivo CSV", error);
      }
    }
  };

  return (
    <div className="flex flex-col items-center mt-6">
      <input 
        type="file"
        accept=".csv"
        onChange={handleFileChange}
        className="w-full max-w-lg px-4 py-2 border border-gray-500 rounded-lg bg-transparent text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-white font-light"
      />
    </div>
  );
};


const ExcPage: React.FC = () => {
  return (
    <div className="min-h-screen bg-gradient-to-b from-[#333641] to-[#282A32] font-sans">
      <Header />
      <Title />
      <FileUpload1 />
      <p className="text-white text-center mt-6">ou</p>
      <KNRInput />
      <ConfirmButton />
    </div>
  );
};

export default ExcPage;
