import { useState } from "react";
import PriceBarChart from "../BarChart/PriceBarChart";
import StandardBarChart from "../BarChart/StandardBarChart";
import ContAreaChart from "../AreaChart/ContAreaChart";
import DiscreteAreaChart from "../AreaChart/DiscreteAreaChart";

import allPriceData from "../../data/priceData.json";
import allEnergyData from "../../data/energyData.json";

const priceData = allPriceData.priceData;
const energyData = allEnergyData.energyData;

const ToggleScreen = () => {
  const [currentChartData, setCurrentChartData] = useState(true);
  const [currentChartType, setCurrentChartType] = useState(true);
  return (
    <>
      <div className='mt-5'>
        {currentChartData && currentChartType && (
          <ContAreaChart
            dataSource={energyData}
            dataKey='EnergyUsage'
            title='24 hour Energy Usage Data'
          />
        )}
        {currentChartData && !currentChartType && (
          <StandardBarChart
            dataSource={energyData}
            dataKey='EnergyUsage'
            title='24 hour Energy Usage Data'
          />
        )}
        {!currentChartData && currentChartType && (
          <DiscreteAreaChart
            dataSource={priceData}
            dataKey='Price'
            title='24 hour Energy Price Data'
          />
        )}
        {!currentChartData && !currentChartType && (
          <StandardBarChart
            dataSource={priceData}
            dataKey='Price'
            title='24 hour Energy Price Data'
          />
        )}
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
