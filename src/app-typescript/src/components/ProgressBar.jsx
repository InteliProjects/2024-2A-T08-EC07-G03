import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
const ProgressBar = ({ progress }) => {
    const navigate = useNavigate();
    useEffect(() => {
        if (progress === 100) {
            navigate('/trained');
        }
    }, [progress, navigate]);
    return (<div className="w-64 bg-gray-700 rounded-full h-2.5 mt-8 itens-center">
      <div className="bg-blue-500 h-2.5 rounded-full" style={{ width: `${progress}%` }}/>
    </div>);
};
export default ProgressBar;
