import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

interface ProgressBarProps {
  progress: number;
}

const ProgressBar: React.FC<ProgressBarProps> = ({ progress }) => {
    const navigate = useNavigate();

    useEffect(() => {
        if (progress === 100) {
          navigate('/trained');
        }
      }, [progress, navigate]);
  return (
    <div className="w-64 bg-gray-700 rounded-full h-2.5 mt-8">
      <div
        className="bg-blue-500 h-2.5 rounded-full 2-64"
        style={{ width: `${progress}%` }}
      />
    </div>
  );
};

export default ProgressBar;
