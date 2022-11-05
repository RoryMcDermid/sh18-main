const DoubleTooltip = ({ active, payload, label, symbol }) => {
  if (active) {
    return (
      <div className='p-3 bg-[#393939] rounded-sm text-gray-200'>
        {payload[0].value != 0 && (
          <div className='font-bold text-[#e7709f]'>
            {symbol == "£" && "£"} {payload[0].value.toFixed(2)}{" "}
            {symbol == "kWh" && "kWh"}
          </div>
        )}
        {payload[1].value != 0 && (
          <div className='font-bold text-[#76a1e1]'>
            {symbol == "£" && "£"} {payload[1].value.toFixed(2)}{" "}
            {symbol == "kWh" && "kWh"}
          </div>
        )}
        <div>{label}</div>
      </div>
    );
  }
  return null;
};

export default DoubleTooltip;
