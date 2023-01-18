import { FC, useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { BarChart, Button, MultiLineChart } from "../components";
import loadSensorReadingDatav3 from "../hooks/loadSensorReadingsv3";

const CompareScreen: FC = () => {
  let { sensorIDs, startDate, endDate, interval } = useParams();

  const [sensors, setSensor] = useState<string[]>([]);
  const sensorReading = loadSensorReadingDatav3({
    sensorIds: sensorIDs!.replaceAll("-", ","),
    startDate: startDate!,
    endDate: endDate!,
    interval: interval!,
  });

  console.log();
  useEffect(() => {
    setSensor(sensorIDs!.split("-"));
  }, [sensorReading]);

  const [currentChartType, setCurrentChartType] = useState(true);

  return (
    <>
      <div className='h-[85vh] flex flex-row'>
        <div className='basis-9/12'>
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
      </div>
    </>
  );
};

export default CompareScreen;
