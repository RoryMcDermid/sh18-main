import {
  ResponsiveContainer,
  AreaChart,
  XAxis,
  YAxis,
  Area,
  Tooltip,
  CartesianGrid,
} from "recharts";
import CustomTooltip from "../AreaCharts/CustomTooltip";
import allData from "../../data/energyDataAllAMR.json";
import "../AreaCharts/headers.css";
import { useState } from "react";





const IndividualMeter = () => {

const [currentSerialNo, setAMR] = useState("0");
var individualData = allData["serialNo" + currentSerialNo];




  return (
    <div className='mx-5'>
      <h1 className='headers'>AMR {currentSerialNo}</h1>

      <ResponsiveContainer width='100%' height={500}>
        <AreaChart data={individualData}>
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

      <div
          className={`px-4 py-3 bg-gray-400 hover:bg-gray-300 rounded-xl
          text-lg font-semibold cursor-pointer`}
          onClick={() => setAMR(((parseInt(currentSerialNo) + 1) % 22).toString())}
          >
          Next AMR
        </div>
              </div>

  );
};

export default IndividualMeter;
