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
import allData from "../data/priceData.json";

const data = allData.priceData;

const PriceAreaChart = () => {
  return (
    <div className='mx-5'>
      <h1 class='headers'>24 hour Energy Price Data</h1>

      <ResponsiveContainer width='100%' height={500}>
        <AreaChart data={data}>
          <defs>
            <linearGradient id='color' x1='0' y1='0' x2='0' y2='1'>
              <stop offset='0%' stopColor='#ff6600' stopOpacity={0.5} />
              <stop offset='75%' stopColor='#ff6600' stopOpacity={0.07} />
            </linearGradient>
          </defs>
          <Area dataKey='Price' stroke='#ff6600' fill='url(#color)' />

          <XAxis dataKey='Timestamp' />

          <YAxis
            dataKey='Price'
            tickCount={10}
            tickFormatter={(price) => `£${price.toFixed(2)}`}
          />

          <Tooltip content={<CustomTooltip symbol='£' />} />

          <CartesianGrid opacity={0.1} vertical={false} />
        </AreaChart>
      </ResponsiveContainer>
    </div>
  );
};

export default PriceAreaChart;
