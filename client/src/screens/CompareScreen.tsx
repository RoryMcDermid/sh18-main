import { FC, useState, useEffect } from "react";
import { Header, Dropdown, MultiSelectDropdown } from "../components";
import { MultiLineChart } from "../components/Charts";
import allTheData from "../data/myData";
import loadSensorReadingData from "../hooks/loadSensorReadings";
import { loadSensors } from "../hooks/loadSensors";

const CompareScreen: FC = () => {
  const sensorArray = loadSensors();

  const [sensors, setSensor] = useState<string[]>([]);
  const [date, setDate] = useState<string[]>([]);

  const [sensorReading, updateSensorReading] = loadSensorReadingData(
    sensors.join(",")
  );

  const dates = ["m1", "m2", "m3", "m4", "m5"];
  return (
    <>
      <Header />
      <div className="h-[85vh] flex flex-row">
        <div className="basis-9/12">
          <MultiLineChart data={sensorReading} />
          <div className="flex justify-end px-10 py-5">
            <button className="px-5 py-3 text-xl text-white font-semibold bg-slate-800 rounded-lg">
              Bar Chart
            </button>
          </div>
        </div>
        <div className="pt-10 basis-3/12 flex flex-col gap-10 items-center">
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
          <button className="bg-red-100" onClick={() => updateSensorReading()}>
            Tired
          </button>
        </div>
      </div>
    </>
  );
};

export default CompareScreen;
