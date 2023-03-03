import { FC, useState } from "react";
import {
  Button,
  CombinedChart,
  Dropdown,
  SuggestionsCard,
} from "../components";
import { useForecastData, useSensors, useSystems } from "../hooks";

const ForecastScreen: FC = () => {
  const { systems } = useSystems();
  const [selectedSystemID, setSelectedSystemID] = useState<number>();
  const { sensors } = useSensors(selectedSystemID);
  const [selectedSensorID, setSelectedSensorID] = useState("");

  const { chartData, suggestionData } = useForecastData(selectedSensorID);

  const handleChange = (systemName: string) => {
    let selectedSystem = systems.find((s) => s[1] === systemName);
    let systemID = selectedSystem![0];
    setSelectedSystemID(systemID);
  };

  const disableButton = selectedSensorID == "";

  return (
    <div className='flex h-[85vh] gap-6'>
      <div className='flex w-2/3 pl-8'>
        <CombinedChart
          selectedSensors={["Average", "Prediction"]}
          sensorReadings={chartData}
        />
      </div>
      <div className=' w-1/3 pr-8'>
        <div className='flex h-5/6 flex-col '>
          <div className=' flex flex-col gap-5 pb-16'>
            <Dropdown
              label='Select a Building:'
              options={systems.map((system) => {
                return system[1];
              })}
              onChange={(item) => handleChange(item)}
              className='w-full'
            />
            <Dropdown
              label='Select a Smart Meter:'
              options={sensors}
              onChange={(item) => setSelectedSensorID(item)}
              className='w-full'
            />
          </div>
          <div className='pt-2'>
            <SuggestionsCard suggestionData={suggestionData} />
          </div>
        </div>
        <div className='mt-5 flex justify-between'>
          <Button
            text='Enter'
            isDisabled={disableButton}
            handleClick={() => {}}
          />
        </div>
      </div>
    </div>
  );
};

export default ForecastScreen;
