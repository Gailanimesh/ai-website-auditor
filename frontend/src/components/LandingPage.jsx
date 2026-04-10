import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Sparkles, ArrowRight } from 'lucide-react';

export default function LandingPage() {
  const [url, setUrl] = useState('');
  const [focused, setFocused] = useState(false);
  const navigate = useNavigate();

  const handleStart = (e) => {
    e.preventDefault();
    if (!url.startsWith('http')) {
      alert("Please enter a valid URL (http:// or https://)");
      return;
    }
    navigate('/audit', { state: { targetUrl: url } });
  };

  return (
    <div className="flex flex-col space-y-16 animate-in fade-in slide-in-from-bottom-8 duration-700">
      
      {/* Hero Content */}
      <div className="space-y-6 text-center lg:text-left flex flex-col items-center lg:items-start">
        <div className="glass-glass px-4 py-1.5 rounded-full inline-flex items-center gap-2 mb-2">
          <Sparkles size={14} className="text-purple-500" />
          <span className="text-xs uppercase tracking-widest text-zinc-600 font-medium">AI Architecture Scanner</span>
        </div>
        
        <h1 className="text-5xl sm:text-6xl md:text-7xl font-bold tracking-tighter leading-[1.1] text-balance text-zinc-900">
          Illuminating the <span className="text-transparent bg-clip-text bg-gradient-to-r from-cyan-600 to-purple-600">dark corners</span> of your website.
        </h1>
        
        <p className="text-lg text-zinc-600 font-light max-w-xl">
          Instantly evaluate SEO, readability, & accessibility using an intelligent headless browser and macOS-grade visualization.
        </p>
      </div>

      {/* Glass Input Form */}
      <form 
        onSubmit={handleStart} 
        className={`relative w-full transition-all duration-500 ease-out transform ${focused ? 'scale-[1.02]' : 'scale-100'}`}
      >
        {/* Soft Pastel Shadow */}
        <div className={`absolute inset-0 bg-gradient-to-r from-cyan-300 to-purple-300 rounded-2xl blur-xl transition-opacity duration-500 ${focused ? 'opacity-40' : 'opacity-0'}`} />
        
        <div className="glass-panel relative rounded-2xl flex items-center p-2 isolate overflow-hidden group border-black/10">
          {/* Subtle inner highlight */}
          <div className="absolute inset-x-0 top-0 h-px bg-gradient-to-r from-transparent via-white/50 to-transparent" />
          
          <input 
            type="text" 
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            onFocus={() => setFocused(true)}
            onBlur={() => setFocused(false)}
            placeholder="Search https://..."
            className="w-full bg-transparent border-none py-5 px-6 text-xl text-zinc-900 font-light focus:outline-none focus:ring-0 placeholder:text-zinc-400"
            required
          />
          
          <button 
            type="submit"
            className="bg-black/5 hover:bg-black/10 text-zinc-800 p-4 rounded-xl transition-all duration-300 flex items-center justify-center m-1 active:scale-95 border border-black/5"
          >
            <ArrowRight size={24} />
          </button>
        </div>
      </form>
    </div>
  );
}
