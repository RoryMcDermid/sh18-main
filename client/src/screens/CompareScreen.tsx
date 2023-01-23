import { FC, useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { BarChart, Button, MultiLineChart } from "../components";
import loadSensorReadingDatav3 from "../hooks/loadSensorReadingsv3";

interface props {
  peakPriceTimes: string[][];
}

const CompareScreen: FC<props> = ({ peakPriceTimes }) => {
  let { sensorIDs, startDate, endDate, interval } = useParams();

  const [sensors, setSensors] = useState<string[]>([]);
  const sensorReading = loadSensorReadingDatav3({
    sensorIds: sensorIDs!.replaceAll("-", ","),
    startDate: startDate!,
    endDate: endDate!,
    interval: interval!,
  });

  useEffect(() => {
    setSensors(sensorIDs!.split("-"));
    console.table({ sensorReading, peakPriceTimes });
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
