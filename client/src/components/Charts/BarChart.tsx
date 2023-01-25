import { FC } from "react";
import Chart from "react-google-charts";
import { formatChartData } from "../../helpers";

interface props {
  headerRow: string[];
  data: energyReading[][];
  peakPriceTimes: string[][];
}

const BarChart: FC<props> = ({ headerRow, data, peakPriceTimes }) => {
  const annotations = peakPriceTimes.map(([start, end]) => ({
    type: "range",
    x: start,
    x2: end,
    fillColor: "#3F51B5",
    color: "#3F51B5",
    opacity: 0.2,
  }));
  const options = {
    backgroundColor: "#242424",
    legend: { position: "none" },
    hAxis: {
      textStyle: { color: "#ffffff" },
    },
    vAxis: { minValue: 0, textStyle: { color: "#ffffff" } },
    chartArea: { width: "80%", height: "80%" },
    animation: {
      startup: true,
      easing: "linear",
      duration: 700,
    },
    annotations: { annotations },
  };
  return (
    <>
      <Chart
        chartType='ColumnChart'
        width='100%'
        height='500px'
        data={formatChartData(headerRow, data)}
        options={options}
      />
    </>
  );
};

export default BarChart;
