import { BrowserRouter, Routes, Route, useLocation } from "react-router-dom";

import Navbar from "../components/common/Navbar";

import Home from "../pages/Home/Home";
import RegisterContent from "../pages/RegisterContent/RegisterContent";
import Library from "../pages/Library/Library";

function Layout() {
  const location = useLocation();

  return (
    <>
      {location.pathname !== "/" && <Navbar />}

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/register" element={<RegisterContent />} />
        <Route path="/library" element={<Library />} />
      </Routes>
    </>
  );
}

function AppRouter() {
  return (
    <BrowserRouter>
      <Layout />
    </BrowserRouter>
  );
}

export default AppRouter;
