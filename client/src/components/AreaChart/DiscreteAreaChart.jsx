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

const DiscreteAreaChart = (props) => {
  const { dataSource, dataKey, title } = props;

  return (
    <div className='mx-5'>
      <h1 className='headers'>{title}</h1>

      <ResponsiveContainer width='100%' height={500}>
        <AreaChart data={dataSource}>
          <defs>
            <linearGradient id='color' x1='0' y1='0' x2='0' y2='1'>
              <stop offset='0%' stopColor='#ff6600' stopOpacity={0.5} />
              <stop offset='75%' stopColor='#ff6600' stopOpacity={0.07} />
            </linearGradient>
          </defs>

          <Area
            type='stepAfter'
            dataKey={dataKey}
            stroke='#ff6600'
            fill='url(#color)'
          />

          <XAxis dataKey='Timestamp' />

          <YAxis
            dataKey={dataKey}
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
export default DiscreteAreaChart;
