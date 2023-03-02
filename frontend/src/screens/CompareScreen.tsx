import { FC, useEffect, useState } from "react";

import {
  Button,
  ButtonGroup,
  CombinedChart,
  DatePicker,
  Dropdown,
  MultiSelectDropdown,
} from "../components";
import { getPeakWholesalePrices } from "../helpers";
import {
  loadSensorReadingData,
  loadSystems,
  loadWholesalePrice,
  useSensors,
} from "../hooks";

const CompareScreen: FC = () => {
  const [formSelection, setFormSelection] = useState({
    selectedSensors: [] as string[],
    startDate: "",
    endDate: "",
  });

  const { selectedSensors, startDate, endDate } = formSelection;

  const { systems } = loadSystems();
  const [selectedSystem, setSelectedSystem] = useState<system | null>(null);
  const { sensors } = useSensors(selectedSystem);
  const [peakPriceTimes, setPeakPriceTimes] = useState<string[][]>([]);
  const [sensorReadings, setSensorReadings] = useState<energyReading[][]>([]);

  const disableButton = !(
    selectedSensors.length > 0 &&
    startDate !== "" &&
    endDate !== ""
  );

  // once the start and end dates are set,
  // an API call is made to get the wholesale energy price data
  const wholesalePrice = loadWholesalePrice(
    formSelection.startDate,
    formSelection.endDate
  );

  // empty form every time page reloads
  useEffect(() => {
    setFormSelection({
      selectedSensors: [] as string[],
      startDate: "",
      endDate: "",
    });
  }, []);

  // once the wholesale energy price data is available,
  // the peak price start and end times are set accordingly
  useEffect(() => {
    setPeakPriceTimes(getPeakWholesalePrices(wholesalePrice));
  }, [wholesalePrice]);

  // only load sensor readings into chart once all form inputs have been selected or re-selected
  useEffect(() => {
    if (!disableButton) {
      setSensorReadings(
        loadSensorReadingData({
          selectedSensors: selectedSensors,
          startDate: startDate,
          endDate: endDate,
        })
      );
    }
  }, [disableButton]);

  return (
    <div className='flex h-[85vh]'>
      <div className='flex w-2/3'>
        <CombinedChart
          selectedSensors={selectedSensors}
          sensorReadings={sensorReadings}
          peakPriceTimes={peakPriceTimes}
        />
      </div>
      <div className='px-5 w-1/3'>
        <div className='flex flex-col gap-5 h-5/6 justify-center pb-5'>
          <Dropdown
            label='Select a system:'
            options={systems}
            onChange={(item) => setSelectedSystem(item)}
            className='w-full'
            getLabel={(system) => system.SYSTEM_NAME}
          />
          <MultiSelectDropdown
            label='Select sensors:'
            items={sensors}
            state={selectedSensors}
            setState={(e) =>
              setFormSelection({ ...formSelection, selectedSensors: e })
            }
            className='w-full'
          />

          <div className='flex justify-between'>
            <DatePicker
              label='Select a start date:'
              state={startDate}
              setState={(e) =>
                setFormSelection({
                  ...formSelection,
                  startDate: e.target.value,
                })
              }
            />
            <DatePicker
              label='Select an end date:'
              state={endDate}
              setState={(e) =>
                setFormSelection({
                  ...formSelection,
                  endDate: e.target.value,
                })
              }
            />
          </div>
        </div>
        <div className='mt-5 flex justify-between'>
          <Button text='Enter' isDisabled={disableButton} />
        </div>
      </div>
    </div>
  );
};

export default CompareScreen;
