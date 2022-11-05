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
import DoubleTooltip from "../Helpers/DoubleTooltip";
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
  const strokeColor3 = "#00ff00";

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

          <YAxis
            yAxisId='left'
            orientation='left'
            dataKey={dataKey1}
            tickCount={10}
            tickFormatter={(energy) => `${energy.toFixed(2)}`}
          />

          <Area
            data={dataSource2}
            yAxisId='left'
            dataKey={dataKey2}
            stroke={strokeColor2}
            fill='url(#color2)'
          />

          {/* price ------------------------- */}
          {isChecked && (
            <>
              <Area
                data={priceDataSource}
                yAxisId='right'
                dataKey='Price'
                stroke={strokeColor3}
                fill='url(#color3)'
              />

              <YAxis
                yAxisId='right'
                orientation='right'
                dataKey='Price'
                tickCount={14}
                tickFormatter={(price) => `${price.toFixed(2)}`}
              />
            </>
          )}
          {/* price ------------------------- */}
          <Tooltip content={<DoubleTooltip symbol='kWh' />} />

          <CartesianGrid opacity={0.1} vertical={false} />
        </AreaChart>
      </ResponsiveContainer>
      <div className='flex justify-center'>
        <label
          for='default-toggle'
          class='inline-flex relative items-center cursor-pointer'
        >
          <input
            type='checkbox'
            value=''
            id='default-toggle'
            className='sr-only peer'
            onChange={(e) => handleChange(e)}
          />
          <div className="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 dark:peer-focus:ring-blue-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600"></div>
        </label>
      </div>
    </div>
  );
};

export default TripleAreaChart;
