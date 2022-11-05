import { useState } from "react";
import {
  ResponsiveContainer,
  AreaChart,
  XAxis,
  YAxis,
  Area,
  Tooltip,
  CartesianGrid,
} from "recharts";
import TripleTooltip from "../Helpers/TripleTooltip";
import Checkbox from "../Helpers/Checkbox";
import "../Helpers/headers.css";

const TripleAreaChart = (props) => {
  const {
    dataSource1,
    dataKey1,
    dataSource2,
    dataKey2,
    priceDataSource,
    title,
  } = props;

  const strokeColor1 = "#ff0066";
  const strokeColor2 = "#0066ff";
  const strokeColor3 = "#06ff06";

  const [isChecked, setIsChecked] = useState(false);

  const handleChange = (e) => {
    setIsChecked(e.target.checked);
  };

  return (
    <div className='mx-5'>
      <h1 className='headers'>{title}</h1>
      <ResponsiveContainer width='99%' height={500}>
        <AreaChart>
          <defs>
            <linearGradient id='color1' x1='0' y1='0' x2='0' y2='1'>
              <stop offset='0%' stopColor={strokeColor1} stopOpacity={0.5} />
              <stop offset='75%' stopColor={strokeColor1} stopOpacity={0.07} />
            </linearGradient>
            <linearGradient id='color2' x1='0' y1='0' x2='0' y2='1'>
              <stop offset='0%' stopColor={strokeColor2} stopOpacity={0.5} />
              <stop offset='75%' stopColor={strokeColor2} stopOpacity={0.07} />
            </linearGradient>
            <linearGradient id='color3' x1='0' y1='0' x2='0' y2='1'>
              <stop offset='0%' stopColor={strokeColor3} stopOpacity={0.5} />
              <stop offset='75%' stopColor={strokeColor3} stopOpacity={0.07} />
            </linearGradient>
          </defs>
          <XAxis dataKey='Timestamp' allowDuplicatedCategory={false} />

          <Area
            data={dataSource1}
            yAxisId='left'
            dataKey={dataKey1}
            stroke={strokeColor1}
            fill='url(#color1)'
          />

          <Area
            data={dataSource2}
            yAxisId='left'
            dataKey={dataKey2}
            stroke={strokeColor2}
            fill='url(#color2)'
          />

          {isChecked && (
            <>
              <Area
                data={priceDataSource}
                yAxisId='right'
                dataKey='Price'
                stroke={strokeColor3}
                fill='url(#color3)'
              />
            </>
          )}

          <YAxis
            yAxisId='left'
            orientation='left'
            dataKey={dataKey1}
            tickCount={10}
            tickFormatter={(energy) => `${energy.toFixed(2)}`}
          />

          <YAxis
            yAxisId='right'
            orientation='right'
            dataKey='Price'
            tickCount={14}
            tickFormatter={(price) => `${price.toFixed(2)}`}
          />
          <Tooltip content={<TripleTooltip isChecked={isChecked} />} />

          <CartesianGrid opacity={0.1} vertical={false} />
        </AreaChart>
      </ResponsiveContainer>

      <div className='flex justify-end mt-5 mr-20 gap-2'>
        <div className='text-gray-400 font-bold'>Show Price Data</div>

        <Checkbox onChange={(e) => handleChange(e)} />
      </div>
    </div>
  );
};

export default TripleAreaChart;
