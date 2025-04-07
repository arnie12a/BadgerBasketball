import React from 'react';

const Navbar = () => {
  return (
    <nav className="bg-red-700 p-4 flex items-center justify-between shadow-md">
      <div className="flex items-center gap-2">
        <span className="text-white text-lg font-bold">Badger Basketball</span>
      </div>
    </nav>
  );
};

export default Navbar;
