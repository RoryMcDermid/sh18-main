import PriceBarChart from "../BarChart/PriceBarChart.jsx";
import PriceAreaChart from "../AreaChart/PriceAreaChart.jsx";
import EnergyBarChart from "../BarChart/EnergyBarChart.jsx";
import EnergyAreaChart from "../AreaChart/EnergyAreaChart.jsx";
import { useState } from "react";

const ToggleScreen = () => {
  const [currentChartData, setCurrentChartData] = useState(true);
  const [currentChartType, setCurrentChartType] = useState(true);
  return (
    <>
      <div className='mt-5'>
        {currentChartData && currentChartType && <EnergyAreaChart />}
        {currentChartData && !currentChartType && <EnergyBarChart />}
        {!currentChartData && currentChartType && <PriceAreaChart />}
        {!currentChartData && !currentChartType && <PriceBarChart />}
      </div>

      <div className='mt-10 w-full flex justify-center gap-5'>
        <div
          className={`px-4 py-3 bg-gray-400 hover:bg-gray-300 rounded-xl
          text-lg font-semibold cursor-pointer`}
          onClick={() => {
            setCurrentChartData(!currentChartData);
          }}
        >
          {currentChartData ? "Price" : "Energy"}
        </div>
        <div
          className={`px-4 py-3 bg-gray-400 hover:bg-gray-300 rounded-xl
          text-lg font-semibold cursor-pointer`}
          onClick={() => {
            setCurrentChartType(!currentChartType);
          }}
        >
          {currentChartType ? "BarChart" : "AreaChart"}
        </div>
      </div>
    </>
  );
};

export default ToggleScreen;
