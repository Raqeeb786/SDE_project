import { BrowserRouter, Routes, Route } from "react-router-dom";

import LoginPage from "./pages/loginPage";
import HomePage from "./pages/homePage";
import ProtectedRoute from './components/ProtectedRoute';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route
            path="/home"
            element={
                <ProtectedRoute>
                    <HomePage />
                </ProtectedRoute>
            }
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
