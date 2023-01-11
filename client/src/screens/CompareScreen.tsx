import { FC, useState, useEffect } from "react";
import { Header, Dropdown, MultiSelectDropdown } from "../components";
import Button from "../components/Button";
import { MultiLineChart } from "../components/Charts";
import { BarChart } from "../components/Charts";
import loadSensorReadingData from "../hooks/loadSensorReadings";
import { loadSensors } from "../hooks/loadSensors";

const CompareScreen: FC = () => {
  const sensorArray = loadSensors();

  const [sensors, setSensor] = useState<string[]>([]);
  const [date, setDate] = useState<string>("");
  const [currentChartType, setCurrentChartType] = useState(true);
  const [sensorReading, updateSensorReading] = loadSensorReadingData(
    sensors.join(",")
  );

  const dates = ["m1", "m2", "m3", "m4", "m5"];
  const disable = !(sensors.length != 0);

  return (
    <>
      <Header />
      <div className='h-[85vh] flex flex-row'>
        <div className='basis-9/12'>
          {currentChartType && (
            <MultiLineChart headerRow={["", ...sensors]} data={sensorReading} />
          )}
          {!currentChartType && (
            <BarChart headerRow={["", ...sensors]} data={sensorReading} />
          )}
          <div
            className={"flex justify-end px-10 py-5"}
            onClick={() => {
              setCurrentChartType(!currentChartType);
            }}
          >
            <button className='px-5 py-3 text-xl text-white font-semibold bg-slate-800 rounded-lg'>
              {currentChartType ? "BarChart" : "AreaChart"}
            </button>
          </div>
        </div>
        <div className='pt-10 basis-3/12 flex flex-col gap-10 items-center'>
          <div className='px-5 w-full flex start'>
            <Button
              isDisabled={disable}
              text='Select'
              handleClick={() => updateSensorReading()}
            />
          </div>
          <Dropdown
            label={"Select a time period: "}
            state={date}
            setState={setDate}
            items={dates}
          />
          <MultiSelectDropdown
            label={"Select a sensor:"}
            state={sensors}
            setState={setSensor}
            items={sensorArray}
          />
        </div>
      </div>
    </>
  );
};

export default CompareScreen;
