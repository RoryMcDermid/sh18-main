import { FC } from "react";
import Chart from "react-google-charts";
import { formatChartData } from "../../helpers";

interface props {
  headerRow: string[];
  data: energyReading[][];
}

const BarChart: FC<props> = (props) => {
  let { headerRow, data } = props;

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
