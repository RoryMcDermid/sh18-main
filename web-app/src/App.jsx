import PriceBarChart from "./components/BarChart/PriceBarChart.jsx";
import PriceAreaChart from "./components/AreaChart/PriceAreaChart.jsx";
import EnergyBarChart from "./components/BarChart/EnergyBarChart.jsx";
import EnergyAreaChart from "./components/AreaChart/EnergyAreaChart.jsx";
import { useState } from "react";

function App() {
  const [currentChart1, setCurrentChart1] = useState(true);
  const [currentChart2, setCurrentChart2] = useState(true);
  return (
    <>
      <div className='mt-5'>
        {currentChart1 && <EnergyAreaChart />}
          {currentChart2 && <EnergyBarChart />}
        {!currentChart1 && <PriceAreaChart />}
          {!currentChart2 && <PriceBarChart />}

      </div>

      <div className='mt-10 w-full flex justify-center gap-5'>
        <div
          className={`px-4 py-3 bg-gray-400 hover:bg-gray-300 rounded-xl
          text-lg font-semibold cursor-pointer`}
          onClick={() => {setCurrentChart1(!currentChart1);setCurrentChart2(!currentChart2)}}
        >
          {currentChart1 ? "Price" : "Energy"}

        </div>
          <div className={`px-4 py-3 bg-gray-400 hover:bg-gray-300 rounded-xl
          text-lg font-semibold cursor-pointer`}
              onClick={() => {setCurrentChart2(currentChart2) }}>

              {currentChart2 ? "BarChart" : "AreaChart"}
          </div>
      </div>
    </>
  );
}


export default App;

