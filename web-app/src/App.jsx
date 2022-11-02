import { useState } from "react";
import DiscreteAreaChart from "./components/AreaChart/DiscreteAreaChart";
import ContAreaChart from "./components/AreaChart/ContAreaChart";
import allPriceData from "./data/priceData.json";
import allEnergyData from "./data/energyData.json";

const priceData = allPriceData.priceData;
const energyData = allEnergyData.energyData;

function App() {
  const [currentChart, setCurrentChart] = useState(true);
  return (
    <>
      <div className='mt-5'>
        {currentChart && (
          <ContAreaChart
            dataSource={energyData}
            dataKey='EnergyUsage'
            title='24 hour Energy Usage Data'
          />
        )}
        {!currentChart && (
          <DiscreteAreaChart
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
          onClick={() => setCurrentChart(!currentChart)}
        >
          {currentChart ? "Price" : "Energy"}
        </div>
      </div>
    </>
  );
}

export default App;
