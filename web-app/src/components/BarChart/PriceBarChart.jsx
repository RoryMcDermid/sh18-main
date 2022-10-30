import { BarChart, Bar, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import CustomTooltip from "../AreaChart/CustomTooltip";
import allData from "../../data/priceData.json";
import "../AreaChart/headers.css";

const data = allData.priceData;

const PriceBarChart = () => {
  return (
    <div className='mx-5'>
      <h1 className='headers'>24 hour Energy Price Data</h1>
      <ResponsiveContainer width='100%' height={500}>
        <BarChart data={data}>

          <XAxis dataKey='Timestamp' />

          <YAxis
            dataKey='Price'
            tickCount={10}
            tickFormatter={(energy) => `${energy.toFixed(2)}`}
          />

          <Tooltip content={<CustomTooltip symbol='£' />} />
            <Legend />

          <CartesianGrid stroke = "#ccc" />
            <Bar dataKey="Price" fill="#ff6600" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
};

export default PriceBarChart;