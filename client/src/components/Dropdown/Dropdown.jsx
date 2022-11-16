import { useState } from "react";
import { ReactComponent as DownChevron } from "../../assets/chevron-down.svg";
import { ReactComponent as UpChevron } from "../../assets/chevron-up.svg";

const Dropdown = ({ dataSources }) => {
  const [expanded, setExpanded] = useState(false);
  const [option, setOption] = useState("Select a data source to view");

  const handleOption = (option) => {
    setOption(option);
    setExpanded(false);
  };

  return (
    <div className='grid gap-2'>
      <div
        className={`p-6 w-80 h-max flex justify-between 
        rounded-lg bg-slate-700 hover:bg-slate-600 cursor-pointer`}
        onClick={() => setExpanded(!expanded)}
      >
        <p className='text-white font-medium'>{option}</p>
        {expanded ? (
          <UpChevron className='text-white' />
        ) : (
          <DownChevron className='text-white' />
        )}
      </div>
      {expanded && (
        <div className='p-2 w-80 grid grid-cols-1 rounded-lg bg-white top-[7.5rem] absolute'>
          {dataSources.map((singleSource) => (
            <div
              key={singleSource.name}
              className='p-4 rounded-lg hover:bg-gray-200/60 hover:font-semibold cursor-pointer'
              onClick={() => {
                handleOption(singleSource.name);
              }}
            >
              {singleSource.name}
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Dropdown;
