import { useState } from "react";
import { Route, Routes } from "react-router-dom";
import { Header } from "./components";
import { SystemSelectScreen, CompareScreen } from "./screens";

function App() {
  const [peakPriceTimes, setPeakPriceTimes] = useState<string[][]>([]);

  return (
    <>
      <Header />
      <Routes>
        <Route
          path='/'
          element={<SystemSelectScreen setPeakPriceTimes={setPeakPriceTimes} />}
        />
        <Route
          path='/compare/:sensorIDs/:startDate/:endDate/:interval'
          element={<CompareScreen peakPriceTimes={peakPriceTimes} />}
        />
      </Routes>
    </>
  );
}

export default App;
