import { Route, Routes } from "react-router-dom";
import { Header } from "./components";
import { CompareScreen, ForecastScreen } from "./screens";

function App() {
  return (
    <>
      <Header />
      <Routes>
        <Route path='/compare' element={<CompareScreen />} />
        <Route path='/forecast' element={<ForecastScreen />} />
      </Routes>
    </>
  );
}

export default App;
