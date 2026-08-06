import ThemeContextProvider from "./context/ThemeContext";
import AppRouter from "./router/AppRouter";

function App() {
  return (
    <ThemeContextProvider>
      <AppRouter />
    </ThemeContextProvider>
  );
}

export default App;
