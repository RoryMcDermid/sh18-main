import { useState, useEffect } from "react";
import {
  ResponsiveContainer,
  AreaChart,
  XAxis,
  YAxis,
  Area,
  Tooltip,
  CartesianGrid,
} from "recharts";
import CustomTooltip from "../Helpers/CustomTooltip";
import "../Helpers/headers.css";

const ContAreaChart = (props) => {
  const { dataSource, dataKey, title } = props;
  const [strokeColor, setStrokeColor] = useState("#000");

  const handleColor = (dataKey) => {
    if (dataKey == "Price") {
      setStrokeColor("#ff6600");
    } else if (dataKey == "EnergyUsage") {
      setStrokeColor("#cc0000");
    } else if (dataKey == "Cost") {
      setStrokeColor("#006600");
    }
  };

  useEffect(() => {
    handleColor(dataKey);
  });

  return (
    <div className='mx-5'>
      <h1 className='headers'>{title}</h1>

      <ResponsiveContainer width='100%' height={500}>
        <AreaChart data={dataSource}>
          <defs>
            <linearGradient id='color' x1='0' y1='0' x2='0' y2='1'>
              <stop offset='0%' stopColor={strokeColor} stopOpacity={0.5} />
              <stop offset='75%' stopColor={strokeColor} stopOpacity={0.07} />
            </linearGradient>
          </defs>
          <Area dataKey={dataKey} stroke={strokeColor} fill='url(#color)' />

          <XAxis dataKey='Timestamp' />

          <YAxis
            dataKey={dataKey}
            tickCount={10}
            tickFormatter={(energy) => `${energy.toFixed(2)}`}
          />

          <Tooltip content={<CustomTooltip symbol='kWh' />} />

          <CartesianGrid opacity={0.1} vertical={false} />
        </AreaChart>
      </ResponsiveContainer>
    </div>
  );
};

export default ContAreaChart;
