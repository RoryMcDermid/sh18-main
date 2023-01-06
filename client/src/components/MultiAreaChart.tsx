import React, { FC, useState } from "react";
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
  title: string;
}

const MultiAreaChart: FC<props> = ({ dataSource, dataKey, title }) => {
  const strokeColor1 = "#ff0066";
  const strokeColor2 = "#0066ff";

  return (
    <div className='mx-5'>
      <h1 className='ml-20 p-3 text-4xl text-white font-semibold'>{title}</h1>
      <ResponsiveContainer width='99%' height={500}>
        <AreaChart>
          <defs>
            <linearGradient id='color1' x1='0' y1='0' x2='0' y2='1'>
              <stop offset='0%' stopColor={strokeColor1} stopOpacity={0.5} />
              <stop offset='75%' stopColor={strokeColor1} stopOpacity={0.07} />
            </linearGradient>
          </defs>
          <defs>
            <linearGradient id='color2' x1='0' y1='0' x2='0' y2='1'>
              <stop offset='0%' stopColor={strokeColor2} stopOpacity={0.5} />
              <stop offset='75%' stopColor={strokeColor2} stopOpacity={0.07} />
            </linearGradient>
          </defs>
          <XAxis dataKey='DATE_OF_RECORD' allowDuplicatedCategory={false} />

          <Area
            // @ts-ignore
            data={dataSource}
            yAxisId='left'
            dataKey={dataKey}
            stroke={strokeColor1}
            fill='url(#color1)'
          />
          {/* <Area
            data={dataSource2}
            yAxisId='left'
            dataKey={dataKey2}
            stroke={strokeColor2}
            fill='url(#color2)'
          /> */}

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
