import { BarChart, Bar, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import CustomTooltip from "../AreaChart/CustomTooltip";
import allData from "../../data/energyData.json";
import "../AreaChart/headers.css";


const data = allData.energyData;

const EnergyBarChart = () => {
  return (
    <div className='mx-5'>
      <h1 className='headers'>24 hour Energy Usage Data</h1>
      <ResponsiveContainer width='100%' height={500}>
        <BarChart data={data}>

          <XAxis dataKey='Timestamp' />

          <YAxis
            dataKey='EnergyUsage'
            tickCount={10}
            tickFormatter={(energy) => `${energy.toFixed(2)}`}
          />

          <Tooltip content={<CustomTooltip symbol='kWh' />} />
            <Legend />

          <CartesianGrid stroke = "#ccc" />
            <Bar dataKey="EnergyUsage" fill="#cc0000" />
        </BarChart>
      </ResponsiveContainer>

    </div>

  );
};

export default EnergyBarChart;

