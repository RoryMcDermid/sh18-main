const TripleTooltip = ({ active, payload, label, isChecked }) => {
  if (active) {
    return (
      <div className='p-3 bg-[#393939] rounded-sm text-gray-200'>
        {payload[0].value != 0 && (
          <div className='font-bold text-[#e7709f]'>
            {payload[0].value.toFixed(2)} kWh
          </div>
        )}
        {payload[1].value != 0 && (
          <div className='font-bold text-[#76a1e1]'>
            {payload[1].value.toFixed(2)} kWh
          </div>
        )}
        {isChecked && (
          <div className='font-bold text-[#64e960]'>
            £ {payload[2].value.toFixed(2)}
          </div>
        )}
        <div>{label}</div>
      </div>
    );
  }
  return null;
};

export default TripleTooltip;
