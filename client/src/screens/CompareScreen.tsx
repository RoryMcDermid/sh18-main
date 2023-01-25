import React, { FC, useState } from "react";
import { BarChart, Button, MultiLineChart } from "../components";
import { loadSensorReadingData } from "../hooks";

interface props {
  selection: selection;
  peakPriceTimes: string[][];
}

const CompareScreen: FC<props> = ({ selection, peakPriceTimes }) => {
  const { selectedSensors, startDate, endDate, interval } = selection;

  const sensorReading = loadSensorReadingData({
    selectedSensors: selectedSensors,
    startDate: startDate,
    endDate: endDate,
    interval: interval,
  });
  const centerStyle:
      React.CSSProperties = {
    display: 'flex',
    alignItems:'center',
    justifyContent:
    'center'
  };

  const [currentChartType, setCurrentChartType] = useState(true);

  console.table({ selection, peakPriceTimes, selectedSensors });

  return (
    <>
      <div style= {centerStyle} className='h-[85vh] flex flex-row'>
        <div className='basis-9/12'>
          {currentChartType && (
            <MultiLineChart
              headerRow={["", ...selectedSensors]}
              data={sensorReading}
              peakPriceTimes={peakPriceTimes}
            />
          )}
          {!currentChartType && (
            <BarChart
              headerRow={["", ...selectedSensors]}
              data={sensorReading}
              peakPriceTimes={peakPriceTimes}
            />
          )}
          <div style= {centerStyle} className={"flex justify-end px-10 py-5"}>
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
