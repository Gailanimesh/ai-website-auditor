import React from 'react';
import { useLocation, Link, Navigate } from 'react-router-dom';
import { ChevronLeft, Target, FileText } from 'lucide-react';

export default function ResultsDashboard() {
  const location = useLocation();
  const data = location.state?.result;

  if (!data) return <Navigate to="/" />;

  const { url, ai_summary, scores } = data;

  const getScoreColor = (score) => {
    // FIX applied here: Added bg-gradient-to-r so the text-gradient works! Added darker stops for visibility on light themes.
    if (score >= 90) return 'bg-gradient-to-r from-emerald-500 to-teal-500 text-transparent bg-clip-text drop-shadow-[0_4px_10px_rgba(16,185,129,0.2)]';
    if (score >= 70) return 'bg-gradient-to-r from-amber-500 to-orange-500 text-transparent bg-clip-text drop-shadow-[0_4px_10px_rgba(245,158,11,0.2)]';
    return 'bg-gradient-to-r from-rose-500 to-red-600 text-transparent bg-clip-text drop-shadow-[0_4px_10px_rgba(225,29,72,0.2)]';
  };

  return (
    <div className="flex flex-col space-y-8 animate-in fade-in slide-in-from-bottom-8 duration-1000 mt-8">
      
      {/* Header Container */}
      <div className="glass-panel p-8 rounded-3xl relative overflow-hidden group shadow-xl">
        <div className="absolute top-0 right-0 p-8 opacity-10 group-hover:scale-110 transition-transform duration-1000">
          <Target size={120} className="text-cyan-600" />
        </div>
        
        <Link to="/" className="inline-flex glass-glass px-4 py-1.5 rounded-full items-center gap-2 text-[10px] uppercase tracking-widest text-zinc-500 hover:text-zinc-900 border border-black/5 hover:bg-black/5 transition-all mb-6 relative z-10 hover:-translate-x-1 font-medium">
          <ChevronLeft size={12} /> New Audit
        </Link>
        
        <h2 className="text-xs font-mono uppercase tracking-widest text-zinc-500 mb-2 relative z-10 font-bold">Target Profile</h2>
        <h1 className="text-3xl sm:text-4xl font-bold tracking-tighter break-all relative z-10 text-zinc-900">
          {url.replace(/^https?:\/\//, '')}
        </h1>
      </div>

      {/* Metrics Bento Box Row */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        
        <div className="glass-panel p-6 rounded-3xl flex flex-col items-center justify-center space-y-2 hover:-translate-y-1 transition-transform duration-300">
          <span className="text-[10px] font-mono uppercase tracking-widest text-zinc-500 font-bold">SEO Health</span>
          <div className={`text-6xl font-black ${getScoreColor(scores.seo)}`}>
            {scores.seo}
          </div>
        </div>

        <div className="glass-panel p-6 rounded-3xl flex flex-col items-center justify-center space-y-2 hover:-translate-y-1 transition-transform duration-300">
          <span className="text-[10px] font-mono uppercase tracking-widest text-zinc-500 font-bold">Content Mass</span>
          <div className={`text-6xl font-black ${getScoreColor(scores.content)}`}>
            {scores.content}
          </div>
        </div>

        <div className="glass-panel p-6 rounded-3xl flex flex-col items-center justify-center space-y-2 hover:-translate-y-1 transition-transform duration-300 relative overflow-hidden">
          <span className="text-[10px] font-mono uppercase tracking-widest text-zinc-500 font-bold">Semantic Access</span>
          <div className={`text-6xl font-black ${getScoreColor(scores.accessibility)}`}>
            {scores.accessibility}
          </div>
        </div>
      </div>

      {/* AI Summary Block */}
      <div className="glass-panel p-8 rounded-3xl space-y-6 relative overflow-hidden shadow-xl border border-black/10">
        {/* Subtle Background Glow */}
        <div className="absolute -left-20 -top-20 w-64 h-64 bg-purple-200/50 rounded-full blur-[80px]" />
        
        <div className="flex items-center gap-3 relative z-10">
          <div className="p-2 bg-purple-50 rounded-xl border border-purple-100 shadow-sm">
             <FileText size={18} className="text-purple-600" />
          </div>
          <span className="text-xs font-mono uppercase tracking-widest text-purple-700 font-bold tracking-wide">AI Executive Summary</span>
        </div>
        
        <div className="relative z-10 text-base sm:text-lg leading-relaxed text-zinc-800 whitespace-pre-wrap font-medium">
          {ai_summary}
        </div>
      </div>

    </div>
  );
}
