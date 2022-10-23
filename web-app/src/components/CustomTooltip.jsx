const CustomTooltip = ({ active, payload, label }) => {
  if (active) {
    return (
      <div className='p-3 bg-[#393939] rounded-sm text-amber-500'>
        <div className='font-bold'>£{payload[0].value.toFixed(2)}</div>
        <div>{label.substr(0, 5)}</div>
      </div>
    );
  }
  return null;
};

export default CustomTooltip;
