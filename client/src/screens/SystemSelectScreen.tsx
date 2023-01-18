import { FC, useState } from "react";
import {
  ButtonGroup,
  DatePicker,
  Dropdown,
  MultiSelectDropdown,
} from "../components";
import getValidIntervals from "../helpers/getValidIntervals";
import {
  findAveragePrice,
  getPeakWholesalePrices,
} from "../helpers/getPeakWholesalePrices";
import { loadSystems, useSensors } from "../hooks";
import { loadWholesalePrice } from "../hooks/loadWholesalePrice";

const SystemSelectScreen: FC = () => {
  const sensorArray = loadSystems();
  const wholesaleprice = loadWholesalePrice("10-01-2023", "16-01-2023");
  const peaktimes = getPeakWholesalePrices(wholesaleprice);
  console.log(peaktimes);
  const { systems: systemArray } = loadSystems();
  const [selectedSystem, setSelectedSystem] = useState<system | null>(null);

  const { sensors } = useSensors(selectedSystem);
  const [selectedSensors, setSelectedSensors] = useState<string[]>([]);

  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");

  const [dataTimeInterval, setDataTimeInterval] = useState("");

  return (
    <>
      <div className="mx-20 flex flex-col gap-10 w-[40rem] ">
        <Dropdown
          label="Select a system:"
          options={systemArray}
          onChange={(item) => setSelectedSystem(item)}
          classes="w-full"
          getLabel={(system) => system.SYSTEM_NAME}
        />
        <MultiSelectDropdown
          label="Select sensors:"
          items={sensors}
          state={selectedSensors}
          setState={setSelectedSensors}
          classes="w-full"
        />

        <div className="flex gap-10">
          <DatePicker
            label="Select a start date-time:"
            datetime={startDate}
            setDatetime={setStartDate}
          />
          <DatePicker
            label="Select an end date-time:"
            datetime={endDate}
            setDatetime={setEndDate}
          />
        </div>
        <ButtonGroup
          label="Select sensor reading interval:"
          items={["15m", "1h", "4h", "1d"]}
          handleEvent={() => {}}
          disableItems={getValidIntervals(startDate, endDate)}
        />
      </div>
    </>
  );
};

export default SystemSelectScreen;
