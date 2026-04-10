import React from 'react';
import { Outlet, Link } from 'react-router-dom';
import { Layers } from 'lucide-react';

export default function Layout() {
  return (
    <>
      {/* Absolute Ambient Background Orbs */}
      <div className="bg-orb-1" />
      <div className="bg-orb-2" />
      <div className="bg-orb-3" />

      {/* Main Foreground Container */}
      <div className="relative z-10 min-h-screen w-full flex flex-col items-center">
        
        {/* Glass Header */}
        <header className="w-full max-w-6xl px-6 py-8 flex justify-between items-center">
          <Link to="/" className="glass-glass px-5 py-2.5 rounded-full flex items-center gap-2 group hover:bg-white/80 transition-all duration-300">
            <Layers className="text-zinc-500 group-hover:text-purple-600 transition-colors duration-500" size={18} />
            <span className="font-semibold tracking-tighter text-sm text-zinc-800">Obsidian.Labs</span>
          </Link>
        </header>

        {/* Content wrapper */}
        <main className="w-full max-w-3xl px-6 flex-grow flex flex-col justify-center pb-32">
          <Outlet />
        </main>
      </div>
    </>
  );
}
