import { FC, useEffect, useState } from "react";

import {
  Button,
  ButtonGroup,
  CombinedChart,
  DatePicker,
  Dropdown,
  MultiSelectDropdown,
} from "../components";
import { useSensorReadings, useSystems, useSensors } from "../hooks";

const CompareScreen: FC = () => {
  const [formSelection, setFormSelection] = useState({
    selectedSensors: [] as string[],
    startDate: "",
    endDate: "",
  });

  const { selectedSensors, startDate, endDate } = formSelection;

  const { systems } = useSystems();
  const [selectedSystemID, setSelectedSystemID] = useState<number>();
  const { sensors } = useSensors(selectedSystemID);
  const [sensorReadings, setSensorReadings] = useState<(string | number)[][]>(
    []
  );

  const disableButton = !(
    selectedSensors.length > 0 &&
    startDate !== "" &&
    endDate !== ""
  );

  // reset form every time page reloads
  useEffect(() => {
    setFormSelection({
      selectedSensors: [] as string[],
      startDate: "",
      endDate: "",
    });
  }, []);

  // only load sensor readings into chart once all form inputs have been selected or re-selected
  useEffect(() => {
    if (!disableButton) {
      setSensorReadings(
        useSensorReadings({
          selectedSensors: selectedSensors,
          startDate: startDate,
          endDate: endDate,
        })
      );
    }
  }, [disableButton]);

  const handleChange = (systemName: string) => {
    let selectedSystem = systems.find((s) => s.SYSTEM_NAME === systemName);
    let systemID = selectedSystem!.SYSTEM_ID;
    setSelectedSystemID(systemID);
  };

  return (
    <div className='flex h-[85vh]'>
      <div className='flex w-2/3'>
        <CombinedChart
          selectedSensors={selectedSensors}
          sensorReadings={sensorReadings}
        />
      </div>
      <div className='w-1/3 px-5'>
        <div className='flex h-5/6 flex-col justify-center gap-5 pb-5'>
          <Dropdown
            label='Select a Building:'
            options={systems.map((system) => {
              return system.SYSTEM_NAME;
            })}
            onChange={handleChange}
            className='w-full'
          />
          <MultiSelectDropdown
            label='Select Smart Meters:'
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
