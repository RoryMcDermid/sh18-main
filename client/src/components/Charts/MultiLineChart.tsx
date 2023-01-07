import { FC } from "react";
import Chart from "react-google-charts";
import { formatChartData } from "../../helpers";

interface props {
  data: energyReadingArray[];
}

const MultiLineChart: FC<props> = ({ data }) => {
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
        data={formatChartData(data)}
        options={options}
      />
    </>
  );
};

export default MultiLineChart;
