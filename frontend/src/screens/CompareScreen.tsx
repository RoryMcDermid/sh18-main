import { FC, useEffect, useState } from "react";

import {
  Button,
  CombinedChart,
  DatePicker,
  Dropdown,
  MultiSelectDropdown,
} from "../components";
import { useSensorReadings, useSystems, useSensors } from "../hooks";

const CompareScreen: FC = () => {
  const blankForm = {
    selectedSensors: [],
    startDate: "",
    endDate: "",
  };

  // state
  const [selectedSystemID, setSelectedSystemID] = useState<number>();

  // state
  const [formSelection, setFormSelection] = useState<selection>({
    ...blankForm,
  });

  // derived state
  const { systems } = useSystems();
  // derived state
  const { sensors } = useSensors(selectedSystemID);
  // derived state
  const { sensorReadings, getSensorReadings } = useSensorReadings({
    ...blankForm,
  });

  // derived state
  const disableButton =
    formSelection.selectedSensors.length > 0 ||
    formSelection.startDate !== "" ||
    formSelection.endDate !== "";

  // reset form every time page reloads
  useEffect(() => {
    setFormSelection({ ...blankForm });
  }, []);

  const handleChange = (systemName: string) => {
    let selectedSystem = systems.find((s) => s[1] === systemName);
    let systemID = selectedSystem![0];
    setSelectedSystemID(systemID);
  };

  return (
    <div className='flex h-[85vh] gap-6'>
      <div className='flex w-2/3 pl-8'>
        <CombinedChart
          selectedSensors={formSelection.selectedSensors}
          sensorReadings={sensorReadings}
        />
      </div>
      <div className='w-1/3 pr-8'>
        <div className='flex h-5/6 flex-col justify-center gap-5 pb-5'>
          <Dropdown
            label='Select a Building:'
            options={systems.map((system) => {
              return system[1];
            })}
            onChange={handleChange}
            className='w-full'
          />
          <MultiSelectDropdown
            label='Select Smart Meters:'
            items={sensors}
            state={formSelection.selectedSensors}
            setState={(e) =>
              setFormSelection({ ...formSelection, selectedSensors: e })
            }
            className='w-full'
          />

          <div className='flex flex-wrap justify-between gap-6'>
            <DatePicker
              label='Select a start date:'
              state={formSelection.startDate}
              setState={(e) =>
                setFormSelection({
                  ...formSelection,
                  startDate: e.target.value,
                })
              }
            />
            <DatePicker
              label='Select an end date:'
              state={formSelection.endDate}
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
          <Button
            text='Enter'
            isDisabled={disableButton}
            handleClick={() => {
              getSensorReadings({ ...formSelection });
            }}
          />
        </div>
      </div>
    </div>
  );
};

export default CompareScreen;
