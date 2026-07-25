import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "../pages/Home/Home";
import RegisterContent from "../pages/RegisterContent/RegisterContent";
import Library from "../pages/Library/Library";

function AppRouter() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />

        <Route path="/register" element={<RegisterContent />} />

        <Route path="/library" element={<Library />} />
      </Routes>
    </BrowserRouter>
  );
}

export default AppRouter;
