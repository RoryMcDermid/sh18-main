import { FC } from "react";
import Chart from "react-google-charts";

interface props {
  dataSource?: any;
  dataKey?: string;
}

const MultiLineChart: FC<props> = ({ dataSource, dataKey }) => {
  const options = {
    legend: { position: "none" },
    vAxis: { minValue: 0 },
    chartArea: { width: "80%", height: "80%" },
  };
  return (
    <>
      <Chart
        chartType='AreaChart'
        width='100%'
        height='500px'
        data={dataSource}
        options={options}
      />
    </>
  );
};

export default MultiLineChart;
