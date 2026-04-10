import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import LandingPage from './components/LandingPage';
import AuditProgress from './components/AuditProgress';
import ResultsDashboard from './components/ResultsDashboard';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<LandingPage />} />
          <Route path="audit" element={<AuditProgress />} />
          <Route path="results" element={<ResultsDashboard />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
