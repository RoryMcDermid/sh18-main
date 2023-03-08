import { FC } from "react";
import Chart from "react-google-charts";

interface props {
  title: string;
  headerRow: string[];
  data: (string | number)[][];
}

const BarChart: FC<props> = (props) => {
  let { title, headerRow, data } = props;

  const options = {
    title: title,
    titleTextStyle: { color: "#ffffff", fontSize: 16 },
    backgroundColor: "#111827",
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
        data={[headerRow, ...data]}
        options={options}
      />
    </>
  );
};

export default BarChart;
