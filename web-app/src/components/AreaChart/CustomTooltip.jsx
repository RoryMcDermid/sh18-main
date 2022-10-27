const CustomTooltip = ({ active, payload, label, symbol }) => {
  if (active) {
    return (
      <div className='p-3 bg-[#393939] rounded-sm text-gray-200'>
        <div className='font-bold'>
          {symbol == "£" && "£"} {payload[0].value.toFixed(2)}{" "}
          {symbol == "kWh" && "kWh"}
        </div>
        <div>{label}</div>
      </div>
    );
  }
  return null;
};

export default CustomTooltip;
