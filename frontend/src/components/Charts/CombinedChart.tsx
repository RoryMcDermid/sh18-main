import { FC, useEffect, useState } from "react";
import Loading from "react-loading";
import { BarChart, Button, MultiLineChart } from "..";

interface props {
  selectedSensors: string[];
  sensorReadings: energyReading[][];
  peakPriceTimes: string[][];
}

const CombinedChart: FC<props> = (props) => {
  let { selectedSensors, sensorReadings, peakPriceTimes } = props;

  const [currentChartType, setCurrentChartType] = useState(true);
  const [chartReady, setChartReady] = useState(false);

  useEffect(() => {
    if (sensorReadings.length === 0) {
      setChartReady(false);
    } else {
      setChartReady(true);
    }
  }, [sensorReadings]);

  return (
    <div className='flex flex-col w-full'>
      <div className='h-5/6 w-full'>
        {chartReady ? (
          <>
            {currentChartType ? (
              <MultiLineChart
                headerRow={["", ...selectedSensors]}
                data={sensorReadings}
                peakPriceTimes={peakPriceTimes}
              />
            ) : (
              <BarChart
                headerRow={["", ...selectedSensors]}
                data={sensorReadings}
                peakPriceTimes={peakPriceTimes}
              />
            )}
          </>
        ) : (
          <div className='w-full h-full flex justify-center items-center'>
            <Loading type='spin' color='#ffffff' height={50} width={50} />
          </div>
        )}
      </div>
      <div className='mt-5 flex justify-end'>
        <Button
          className='w-max'
          text={currentChartType ? "Bar Chart" : "Line Chart"}
          handleClick={() => setCurrentChartType(!currentChartType)}
        />
      </div>
    </div>
  );
};

export default CombinedChart;
