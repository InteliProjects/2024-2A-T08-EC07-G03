import React from 'react';

interface NavbarProps {
  children: React.ReactNode;
}

const Navbar: React.FC<NavbarProps> = ({ children }) => {
  return (
    <nav className="bg-transparent text-white text-lg m-6">
      {children}
    </nav>
  );
};

export default Navbar;
