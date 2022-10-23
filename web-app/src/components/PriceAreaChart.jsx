import {
  ResponsiveContainer,
  AreaChart,
  XAxis,
  YAxis,
  Area,
  Tooltip,
  CartesianGrid,
} from "recharts";
import CustomTooltip from "./CustomTooltip";
import allData from "../mock-data/data.json";

const data = allData.data;

const PriceAreaChart = () => {
  return (
    <div className='mx-5'>
      <ResponsiveContainer width='100%' height={500}>
        <AreaChart data={data}>
          <defs>
            <linearGradient id='color' x1='0' y1='0' x2='0' y2='1'>
              <stop offset='0%' stopColor='#ff6600' stopOpacity={0.5} />
              <stop offset='75%' stopColor='#ff6600' stopOpacity={0.07} />
            </linearGradient>
          </defs>
          <Area dataKey='Overall' stroke='#ff6600' fill='url(#color)' />

          <XAxis
            dataKey='Timestamp'
            tickFormatter={(timestamp) => timestamp.substr(0, 5)}
          />

          <YAxis
            dataKey='Overall'
            tickCount={10}
            tickFormatter={(price) => `£${price.toFixed(2)}`}
          />

          <Tooltip content={<CustomTooltip />} />

          <CartesianGrid opacity={0.1} vertical={false} />
        </AreaChart>
      </ResponsiveContainer>
    </div>
  );
};

export default PriceAreaChart;
