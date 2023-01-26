import { FC, useEffect, useState } from "react";
import { Link } from "react-router-dom";
import {
  Button,
  ButtonGroup,
  DatePicker,
  Dropdown,
  MultiSelectDropdown,
} from "../components";
import { getValidIntervals } from "../helpers";
import { loadSystems, useSensors } from "../hooks";

interface props {
  formSelection: selection;
  setFormSelection: setter<selection>;
}

const SystemSelectScreen: FC<props> = ({ formSelection, setFormSelection }) => {
  const { selectedSensors, startDate, endDate, interval } = formSelection;

  // makes API call to backend to load all systems into the first dropdown
  const { systems } = loadSystems();
  const [selectedSystem, setSelectedSystem] = useState<system | null>(null);

  // once a system is selected in the first dropdown,
  // its corresponding sensors are loaded into the second dropdown
  const { sensors } = useSensors(selectedSystem);

  useEffect(() => {
    console.table(formSelection);
    setFormSelection({
      selectedSensors: [] as string[],
      endDate: "",
      startDate: "",
      interval: -1,
    });
  }, []);

  const disableButton = !(
    selectedSensors.length > 0 &&
    startDate != "" &&
    endDate != "" &&
    interval >= 1 &&
    interval <= 4
  );

  return (
    <div className='mb-20 flex '>
      <div className='mx-20 flex flex-col gap-10 w-[40rem] '>
        <Dropdown
          label='Select a system:'
          options={systems}
          onChange={(item) => setSelectedSystem(item)}
          classes='w-full'
          getLabel={(system) => system.SYSTEM_NAME}
        />
        <MultiSelectDropdown
          label='Select sensors:'
          items={sensors}
          state={selectedSensors}
          setState={(e) =>
            setFormSelection({
              ...formSelection,
              selectedSensors: e,
            })
          }
          classes='w-full'
        />

        <div className='flex gap-10'>
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
        <ButtonGroup
          label='Select sensor reading interval:'
          items={["15m", "1h", "4h", "1d"]}
          handleSelection={(i) =>
            setFormSelection({
              ...formSelection,
              interval: i,
            })
          }
          disableItems={getValidIntervals(startDate, endDate)}
        />
      </div>
      <div className='mt-10'>
        <Link to='/compare'>
          <Button text='Enter' isDisabled={disableButton} />
        </Link>
      </div>
    </div>
  );
};

export default SystemSelectScreen;
