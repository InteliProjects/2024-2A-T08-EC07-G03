import React from 'react';

const FileUpload: React.FC = () => {
    return (
      <div className="font-sans flex flex-col items-center justify-center border-2 border-dashed bg-gradient-to-b from-[#333641] to-[#2D3039] h-64 w-full max-w-lg mx-auto mt-10 bg-gray-800 rounded-lg">
        <label className="cursor-pointer">
          <div className="flex flex-col items-center space-y-2">
            <svg width="150" height="150" viewBox="0 0 150 150" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="40" y="70" width="70" height="40" rx="5" stroke="#888888" stroke-width="6" />
            <circle cx="95" cy="90" r="4" fill="#888888" />
            <path d="M75 30 L75 80" stroke="#888888" stroke-width="6" stroke-linecap="round" />
            <path d="M60 45 L75 30 L90 45" stroke="#888888" stroke-width="6" stroke-linecap="round" />
            </svg>
            <p className="text-white">Adicione seu .csv para treinar o modelo</p>
          </div>
          <input type="file" accept=".csv" className="hidden" />
        </label>
      </div>
    );
  };

export default FileUpload;
