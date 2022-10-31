import {
  ResponsiveContainer,
  AreaChart,
  XAxis,
  YAxis,
  Area,
  Tooltip,
  CartesianGrid,
} from "recharts";
import CustomTooltip from "./CustomTooltip2";
import allData from "../../data/energyData.json";

const data = allData.energyData;

const EnergyAreaChart = () => {
  return (
    <div className='mx-5'>
      <h1 className='text-3xl text-center text-white font-bold mb-5'>
        24 hour Energy Usage Data
      </h1>

      <ResponsiveContainer className='absolute' width={"78%"} height={400}>
        <AreaChart data={data}>
          <defs>
            <linearGradient id='color' x1='0' y1='0' x2='0' y2='1'>
              <stop offset='0%' stopColor='#cc0000' stopOpacity={0.5} />
              <stop offset='75%' stopColor='#cc0000' stopOpacity={0.07} />
            </linearGradient>
          </defs>
          <Area dataKey='EnergyUsage' stroke='#cc0000' fill='url(#color)' />

          <XAxis dataKey='Timestamp' />

          <YAxis
            dataKey='EnergyUsage'
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

export default EnergyAreaChart;
