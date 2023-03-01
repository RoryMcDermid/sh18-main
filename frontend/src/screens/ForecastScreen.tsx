import { FC } from "react";
import { CombinedChart, SuggestionsCard } from "../components";

const ForecastScreen: FC = () => {
  const suggestionData = [1, 2, 3, 4];

  return (
    <div className='flex h-[85vh]'>
      <div className='w-2/3'>
        <CombinedChart
          selectedSensors={[]}
          sensorReadings={[]}
          peakPriceTimes={[]}
        />
      </div>
      <div className='w-1/3'>
        <SuggestionsCard suggestionData={suggestionData} />
      </div>
    </div>
  );
};

export default ForecastScreen;
