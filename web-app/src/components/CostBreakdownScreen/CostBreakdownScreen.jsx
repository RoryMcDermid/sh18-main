import {
  ResponsiveContainer,
  AreaChart,
  XAxis,
  YAxis,
  Area,
  Tooltip,
  CartesianGrid,
} from "recharts";
import CustomTooltip from "../Helpers/CustomTooltip.jsx";
import costData from "../../data/CostData.json";
import "../Helpers/headers.css";
import ContAreaChart from "../AreaChart/ContAreaChart.jsx";

const data = costData.CostData;

const CostBreakdownScreen = () => {
  return (
    <ContAreaChart
      dataSource={data}
      dataKey='Cost'
      title='Total Cost per hour'
    />
  );
};

export default CostBreakdownScreen;
