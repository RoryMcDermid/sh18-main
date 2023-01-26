import { useEffect, useState } from "react";
import { Route, Routes } from "react-router-dom";
import { Header } from "./components";
import { getPeakWholesalePrices } from "./helpers";
import { loadWholesalePrice } from "./hooks";
import { SystemSelectScreen, CompareScreen } from "./screens";

function App() {
  const [formSelection, setFormSelection] = useState<selection>({
    selectedSensors: [],
    startDate: "",
    endDate: "",
    interval: -1,
  });

  const [peakPriceTimes, setPeakPriceTimes] = useState<string[][]>([]);

  console.log({ peakPriceTimes });

  // once the start and end dates are set,
  // an API call is made to get the wholesale energy price data
  const wholesalePrice = loadWholesalePrice(
    formSelection.startDate,
    formSelection.endDate
  );

  // once the wholesale energy price data is available,
  // the peak price start and end times are set accordingly
  useEffect(() => {
    setPeakPriceTimes(getPeakWholesalePrices(wholesalePrice));
  }, [wholesalePrice]);
  return (
    <>
      <Header />
      <Routes>
        <Route
          path='/'
          element={
            <SystemSelectScreen
              formSelection={formSelection}
              setFormSelection={setFormSelection}
            />
          }
        />
        <Route
          path='/compare'
          element={
            <CompareScreen
              peakPriceTimes={peakPriceTimes}
              selection={formSelection}
            />
          }
        />
      </Routes>
    </>
  );
}

export default App;