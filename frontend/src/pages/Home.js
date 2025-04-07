import React from 'react';

const Home = () => {
  return (
    <div className="flex flex-col items-center justify-center h-[80vh] text-center">
      <img src="/assets/badger-icon.png" alt="Badger Icon" className="w-20 h-20 mb-4" />
      <h1 className="text-4xl font-extrabold text-red-800">Welcome to Badger Basketball</h1>
      <p className="mt-2 text-gray-700">Track stats, explore players, and dive into Wisconsin hoops.</p>
    </div>
  );
};

export default Home;
