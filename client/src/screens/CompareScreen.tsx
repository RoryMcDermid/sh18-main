import { FC, useState } from "react";
import { Header, Dropdown, MultiSelectDropdown, Button } from "../components";
import { BarChart, MultiLineChart } from "../components/Charts";
import { loadSensorReadingData, loadSensors } from "../hooks";

const CompareScreen: FC = () => {
  const sensorArray = loadSensors();

  const [sensors, setSensor] = useState<string[]>([]);
  const [sensorReading, updateSensorReading] = loadSensorReadingData(
    sensors.join(",")
  );

  const dates = ["m1", "m2", "m3", "m4", "m5"];
  const [date, setDate] = useState<string>("");

  const [currentChartType, setCurrentChartType] = useState(true);

  const disable = !(sensors.length != 0);

  return (
    <>
      <div className="h-[85vh] flex flex-row">
        <div className="basis-9/12">
          {currentChartType && (
            <MultiLineChart headerRow={["", ...sensors]} data={sensorReading} />
          )}
          {!currentChartType && (
            <BarChart headerRow={["", ...sensors]} data={sensorReading} />
          )}
          <div className={"flex justify-end px-10 py-5"}>
            <Button
              text={currentChartType ? "BarChart" : "AreaChart"}
              handleClick={() => setCurrentChartType(!currentChartType)}
            />
          </div>
        </div>
        <div className="pt-10 px-10 basis-3/12 flex flex-col gap-10 items-start">
          <div className="w-full flex start">
            <Button
              isDisabled={disable}
              text="Select"
              handleClick={() => updateSensorReading()}
            />
          </div>
          <Dropdown
            label={"Select a time period: "}
            state={date}
            setState={setDate}
            options={dates}
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
