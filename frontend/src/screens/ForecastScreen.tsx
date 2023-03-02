import { FC, useState } from "react";
import { CombinedChart, Dropdown, SuggestionsCard } from "../components";
import { useForecastData, useSensors, useSystems } from "../hooks";

const ForecastScreen: FC = () => {
  const { systems } = useSystems();
  const [selectedSystemID, setSelectedSystemID] = useState<number>();
  const { sensors } = useSensors(selectedSystemID);
  const [selectedSensor, setSelectedSensor] = useState("");

  const { chartData, suggestionData } = useForecastData(selectedSensor);

  const handleChange = (systemName: string) => {
    let selectedSystem = systems.find((s) => s.SYSTEM_NAME === systemName);
    let systemID = selectedSystem!.SYSTEM_ID;
    setSelectedSystemID(systemID);
  };
  return (
    <div className='flex h-[85vh]'>
      <div className='flex w-2/3'>
        <CombinedChart
          selectedSensors={["", "Average", "Prediction"]}
          sensorReadings={chartData}
        />
      </div>
      <div className='px-5 w-1/3  h-5/6'>
        <div className='flex flex-col gap-5 pb-16'>
          <Dropdown
            label='Select a Building:'
            options={systems.map((system) => {
              return system.SYSTEM_NAME;
            })}
            onChange={(item) => handleChange(item)}
            className='w-full'
          />
          <Dropdown
            label='Select a Smart Meter:'
            options={sensors}
            onChange={(item) => setSelectedSensor(item)}
            className='w-full'
          />
        </div>
        <div className='pt-2'>
          <SuggestionsCard suggestionData={suggestionData} />
        </div>
      </div>
    </div>
  );
};

export default ForecastScreen;
