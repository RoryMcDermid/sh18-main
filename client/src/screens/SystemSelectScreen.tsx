import { FC, useEffect, useState } from "react";
import {
  ButtonGroup,
  DatePicker,
  Dropdown,
  MultiSelectDropdown,
} from "../components";
import { getPeakWholesalePrices, getValidIntervals } from "../helpers";
import { loadSystems, loadWholesalePrice, useSensors } from "../hooks";

const SystemSelectScreen: FC = () => {
  const { systems } = loadSystems();
  const [selectedSystem, setSelectedSystem] = useState<system | null>(null);

  const { sensors } = useSensors(selectedSystem);
  const [selectedSensors, setSelectedSensors] = useState<string[]>([]);

  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");

  const wholesalePrice = loadWholesalePrice(startDate, endDate);

  useEffect(() => {
    const peakPriceTimes = getPeakWholesalePrices(wholesalePrice);
    console.log({ peakPriceTimes });
  }, [wholesalePrice]);

  return (
    <>
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
          setState={setSelectedSensors}
          classes='w-full'
        />

        <div className='flex gap-10'>
          <DatePicker
            label='Select a start date:'
            datetime={startDate}
            setDatetime={setStartDate}
          />
          <DatePicker
            label='Select an end date:'
            datetime={endDate}
            setDatetime={setEndDate}
          />
        </div>
        <ButtonGroup
          label='Select sensor reading interval:'
          items={["15m", "1h", "4h", "1d"]}
          handleEvent={() => {}}
          disableItems={getValidIntervals(startDate, endDate)}
        />
      </div>
    </>
  );
};

export default SystemSelectScreen;
