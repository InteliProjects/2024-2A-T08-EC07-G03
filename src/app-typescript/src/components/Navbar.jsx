import React from 'react';
const Navbar = ({ children }) => {
    return (<nav className="bg-transparent text-white text-lg m-6">
      {children}
    </nav>);
};
export default Navbar;
