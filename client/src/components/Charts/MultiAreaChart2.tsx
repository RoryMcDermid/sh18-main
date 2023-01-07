import { FC, useEffect } from "react";
import {
  ResponsiveContainer,
  AreaChart,
  XAxis,
  YAxis,
  Area,
  Tooltip,
  CartesianGrid,
} from "recharts";

interface props {
  dataSource: energyReadingArray;
  dataKey: string;
  title?: string;
}

const MultiAreaChart: FC<props> = ({ dataSource, dataKey, title }) => {
  const strokeColor = "#ff0066";
  useEffect(() => {
    console.log("here");
  }, []);

  return (
    <div className='mx-5'>
      <div className='ml-20 p-3 text-4xl text-white font-semibold'>{title}</div>
      <ResponsiveContainer width='99%' height={500}>
        <AreaChart>
          <defs>
            <linearGradient id='color1' x1='0' y1='0' x2='0' y2='1'>
              <stop offset='0%' stopColor={strokeColor} stopOpacity={0.5} />
              <stop offset='75%' stopColor={strokeColor} stopOpacity={0.07} />
            </linearGradient>
          </defs>

          <Area
            // @ts-ignore
            data={dataSource}
            yAxisId='left'
            dataKey={dataKey}
            stroke={strokeColor}
            fill='url(#color1)'
          />

          <XAxis dataKey='DATE_OF_RECORD' allowDuplicatedCategory={false} />

          <YAxis
            yAxisId='left'
            orientation='left'
            dataKey={dataKey}
            tickCount={10}
            tickFormatter={(energy) => `${energy.toFixed(2)}`}
          />

          <Tooltip />
          <CartesianGrid opacity={0.1} vertical={false} />
        </AreaChart>
      </ResponsiveContainer>
    </div>
  );
};

export default MultiAreaChart;
