import PriceAreaChart from "./components/PriceAreaChart";
import EnergyAreaChart from "./components/EnergyAreaChart";
import { useState } from "react";

function App() {
  const [currentChart, setCurrentChart] = useState(true);
  return (
    <>
      <div className='mt-48'>
        {currentChart && <EnergyAreaChart />}
        {!currentChart && <PriceAreaChart />}
      </div>
      <div className='mt-10 w-full flex justify-center gap-5'>
        <div
          className={`px-4 py-3 bg-gray-400 hover:bg-gray-300 rounded-xl
          text-lg font-semibold cursor-pointer`}
          onClick={() => setCurrentChart(!currentChart)}
        >
          {currentChart ? "Energy" : "Price"}
        </div>
      </div>
    </>
  );
}

export default App;
