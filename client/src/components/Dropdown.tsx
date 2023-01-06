import { FC, useState } from "react";
import Down from "./chevron-down";
import Up from "./chevron-up";

interface props {
  label: string;
  sensors: string[];
  state: string;
  setState: (newValue: string) => void;
}

const Dropdown: FC<props> = ({ label, sensors, state, setState }) => {
  const [expanded, setExpanded] = useState(false);

  const handleOption = (option: string) => {
    setState(option);
    setExpanded(false);
  };

  return (
    <div>
      <div className='pb-3 pl-1 text-xl text-white'>{label}</div>
      <div className='grid gap-2 relative'>
        <div
          className={`p-6 w-80 h-max flex justify-between 
        rounded-lg bg-slate-800 hover:bg-slate-600 cursor-pointer`}
          onClick={() => setExpanded(!expanded)}
        >
          <p className='text-white font-medium'>{state}</p>
          {expanded ? <Up /> : <Down />}
        </div>
        {expanded && (
          <div className='p-2 w-80 grid grid-cols-1 rounded-lg bg-slate-700 absolute translate-y-[80px] z-10'>
            {sensors.map((sensor) => (
              <div
                key={sensor}
                className='p-4 rounded-lg hover:bg-gray-200/60 text-white hover:text-black hover:font-semibold cursor-pointer'
                onClick={() => {
                  handleOption(sensor);
                }}
              >
                {sensor}
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default Dropdown;
