import { FC, useState, useEffect } from "react";
import { Header, Dropdown, MultiSelectDropdown } from "../components";
import { MultiLineChart } from "../components/Charts";
import allTheData from "../data/myData";
import { loadSensors } from "../hooks/loadSensors";
import useLoadSensorReadingData from "../hooks/loadSensorReadings";

const CompareScreen: FC = () => {
  const sensorArray = loadSensors();

  const [sensorReadingsArray, setSensorReadingsArray] = useState<any>([]);

  const [sensors, setSensor] = useState<string[]>([]);
  const [date, setDate] = useState<string[]>([]);

  const loadData = async () => {
    const sensorData = await Promise.all(
      sensors.map(async (sensor) => {
        const data = await useLoadSensorReadingData(sensor);
        return data;
      })
    );
    setSensorReadingsArray(sensorData);
  };

  useEffect(() => {
    loadData();
  }, [sensors]);

  const dates = ["m1", "m2", "m3", "m4", "m5"];
  return (
    <>
      <Header />
      <div className="h-[85vh] flex flex-row">
        <div className="basis-9/12">
          <MultiLineChart data={sensorReadingsArray} />
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
        </div>
      </div>
    </>
  );
};

export default CompareScreen;
