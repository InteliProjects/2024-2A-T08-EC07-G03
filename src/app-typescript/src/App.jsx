import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import TrainingPage from './pages/TrainingPage';
import TrainingProgressPage from './pages/TrainingProgressPage';
import TrainedModelPage from './pages/TrainedModelPage';
import ExcPage from './pages/ExcPage';
import ExcProgressPage from './pages/ExcProgressPage';
import ExcModelPage from './pages/ExcModelPage';
function App() {
    return (<Router>
      <Routes>
        <Route path="/" element={<Home />}/>
        <Route path="/training" element={<TrainingPage />}/>
        <Route path="/progress" element={<TrainingProgressPage />}/>
        <Route path="/trained" element={<TrainedModelPage />}/>
        <Route path="/exc" element={<ExcPage />}/>
        <Route path="/excProgress" element={<ExcProgressPage />}/>
        <Route path="/excModel" element={<ExcModelPage />}/>
      </Routes>
    </Router>);
}
export default App;
