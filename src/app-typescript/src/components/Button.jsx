import React from 'react';
const Button = ({ label, onClick }) => {
    return (<button className="px-10 py-2 bg-white text-gray-900 rounded-lg hover:bg-gray-200 transition duration-200" onClick={onClick}>
      {label}
    </button>);
};
export default Button;
