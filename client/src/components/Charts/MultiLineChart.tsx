import { FC } from "react";
import Chart from "react-google-charts";
import { formatChartData } from "../../helpers";

interface props {
  headerRow: string[];
  data: energyReading[][];
}

const MultiLineChart: FC<props> = ({ headerRow, data }) => {
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
        data={formatChartData(headerRow, data)}
        options={options}
      />
    </>
  );
};

export default MultiLineChart;
