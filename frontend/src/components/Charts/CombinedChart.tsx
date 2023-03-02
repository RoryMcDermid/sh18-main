import { FC, useEffect, useState } from "react";
import Loading from "react-loading";
import { BarChart, Button, MultiLineChart } from "..";

interface props {
  selectedSensors: string[];
  sensorReadings: energyReading[][];
}

const CombinedChart: FC<props> = (props) => {
  let { selectedSensors, sensorReadings } = props;

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
    <div className='flex w-full flex-col'>
      <div className='h-5/6 w-full'>
        {chartReady ? (
          <>
            {currentChartType ? (
              <MultiLineChart
                headerRow={["", ...selectedSensors]}
                data={sensorReadings}
              />
            ) : (
              <BarChart
                headerRow={["", ...selectedSensors]}
                data={sensorReadings}
              />
            )}
          </>
        ) : (
          <div className='flex h-full w-full items-center justify-center'>
            <Loading type='spin' color='#ffffff' height={50} width={50} />
          </div>
        )}
      </div>
      <div className='mt-5 flex justify-end'>
        <Button
          className='w-max'
          text={currentChartType ? "Bar Chart" : "Line Chart"}
          handleClick={() => setCurrentChartType(!currentChartType)}
          isDisabled={!chartReady}
        />
      </div>
    </div>
  );
};

export default CombinedChart;
