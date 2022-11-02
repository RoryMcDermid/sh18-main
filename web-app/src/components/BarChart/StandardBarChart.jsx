import { useState, useEffect } from "react";
import {
  BarChart,
  Bar,
  Cell,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";
import CustomTooltip from "../AreaChart/CustomTooltip";
import "../AreaChart/headers.css";

const StandardBarChart = (props) => {
  const { dataSource, dataKey, title } = props;

  const [strokeColor, setStrokeColor] = useState("#000");

  const handleColor = (dataKey) => {
    if (dataKey == "Price") {
      setStrokeColor("#ff6600");
    } else {
      setStrokeColor("#cc0000");
    }
  };

  useEffect(() => {
    handleColor(dataKey);
  });

  return (
    <div className='mx-5'>
      <h1 className='headers'>{title}</h1>
      <ResponsiveContainer width='100%' height={500}>
        <BarChart data={dataSource}>
          <XAxis dataKey='Timestamp' />

          <YAxis
            dataKey={dataKey}
            tickCount={10}
            tickFormatter={(energy) => `${energy.toFixed(2)}`}
          />

          <Tooltip content={<CustomTooltip symbol='kWh' />} />
          <Legend />

          <CartesianGrid opacity={0.1} vertical={false} />
          <Bar dataKey={dataKey} fill={strokeColor} />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
};

export default StandardBarChart;
