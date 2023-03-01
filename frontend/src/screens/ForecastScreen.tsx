import { FC, useState } from "react";
import { CombinedChart, SuggestionsCard } from "../components";
import { useForecastData } from "../hooks";

const ForecastScreen: FC = () => {
  const [selectedSensor, setSelectedSensor] = useState("");
  const { chartData, suggestionData } = useForecastData(selectedSensor);

  return (
    <div className='flex h-[85vh]'>
      <div className='flex w-2/3'>
        <CombinedChart
          selectedSensors={["", "Average", "Prediction"]}
          sensorReadings={chartData}
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
