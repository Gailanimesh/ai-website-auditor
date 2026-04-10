import React, { useEffect, useState, useRef } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { Activity } from 'lucide-react';

export default function AuditProgress() {
  const location = useLocation();
  const navigate = useNavigate();
  const targetUrl = location.state?.targetUrl;

  const [logs, setLogs] = useState([]);
  const [currentStatus, setCurrentStatus] = useState("Establishing secure tunnel...");
  const [error, setError] = useState(null);
  const logEndRef = useRef(null);

  useEffect(() => {
    if (!targetUrl) {
      navigate('/');
      return;
    }

    const ws = new WebSocket('ws://localhost:8000/ws/audit');

    ws.onopen = () => ws.send(targetUrl);

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.error) {
        setError(data.error);
        return;
      }
      if (data.log) {
        setCurrentStatus(data.log);
        setLogs(prev => [...prev, data.log]);
      }
      if (data.result) {
        setTimeout(() => navigate('/results', { state: { result: data.result } }), 1200);
      }
    };

    return () => ws.close();
  }, [targetUrl, navigate]);

  useEffect(() => {
    logEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [logs]);

  if (error) {
    return (
      <div className="glass-panel p-8 rounded-3xl text-center space-y-6">
        <div className="mx-auto w-16 h-16 bg-red-100 border border-red-200 rounded-full flex items-center justify-center text-red-500 text-2xl font-bold">!</div>
        <h2 className="text-2xl font-bold text-zinc-900">Audit Failed</h2>
        <p className="text-red-600 bg-red-50 p-4 rounded-xl font-mono text-sm border border-red-100">{error}</p>
        <button onClick={() => navigate('/')} className="glass-glass px-6 py-3 rounded-full text-zinc-800 hover:bg-black/5 transition font-medium">Return Home</button>
      </div>
    );
  }

  return (
    <div className="w-full flex flex-col items-center justify-center space-y-12 animate-in fade-in duration-500 py-12">
      
      {/* HUD Scanner Animation */}
      <div className="relative flex justify-center items-center w-40 h-40">
        <div className="absolute inset-0 bg-cyan-200/50 rounded-full blur-3xl animate-pulse" />
        <div className="w-full h-full rounded-full border border-black/10 border-t-cyan-500 animate-spin-minimal" />
        <div className="w-[80%] h-[80%] absolute rounded-full border border-purple-200/50 border-b-purple-500 animate-[spin-minimal_3s_linear_infinite_reverse]" />
        <Activity className="absolute text-zinc-800 animate-pulse" size={32} />
      </div>

      <div className="text-center space-y-3 relative z-10 w-full">
        <div className="inline-flex glass-glass px-3 py-1 rounded-full text-[10px] uppercase font-mono tracking-widest text-cyan-700 bg-cyan-50/50 border-cyan-100 mb-2">
          Executing Phase
        </div>
        <h2 className="text-2xl font-medium tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-zinc-900 to-zinc-600 h-10 w-full text-balance">
          {currentStatus}
        </h2>
      </div>

      {/* Glass Terminal Feed */}
      <div className="glass-panel w-full rounded-2xl overflow-hidden relative shadow-xl">
        <div className="bg-white/50 px-4 py-2 border-b border-black/5 flex gap-2 items-center">
          <div className="w-3 h-3 rounded-full bg-red-400" />
          <div className="w-3 h-3 rounded-full bg-yellow-400" />
          <div className="w-3 h-3 rounded-full bg-green-400" />
        </div>
        
        <div className="p-6 font-mono text-[11px] text-zinc-600 h-48 overflow-y-auto space-y-2 relative bg-white/30 backdrop-blur-3xl">
          {logs.map((log, i) => (
            <div key={i} className="flex gap-4 animate-in slide-in-from-left-2 duration-300">
              <span className="text-cyan-600/50">[{new Date().toISOString().split('T')[1].slice(0,8)}]</span>
              <span className="text-zinc-800">{log}</span>
            </div>
          ))}
          <div ref={logEndRef} />
        </div>
      </div>
      
    </div>
  );
}
