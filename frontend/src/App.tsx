import { Route, Routes } from "react-router-dom";
import { Header } from "./components";
import { CompareScreen } from "./screens";
import ForecastScreen from "./screens/ForecastScreen";
import LandingScreen from "./screens/LandingScreen";

function App() {
  return (
    <>
      <Header />
      <Routes>
        <Route path="/" element={<LandingScreen />} />
        <Route path="/compare" element={<CompareScreen />} />
        <Route path="/forecast" element={<ForecastScreen />} />
      </Routes>
    </>
  );
}

export default App;
