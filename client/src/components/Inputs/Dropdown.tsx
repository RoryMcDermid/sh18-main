import { FC, useState } from "react";
import { ChevronUp, ChevronDown } from "../SVGs";

interface props {
  label: string;
  options: system[];
  getLabel: (option: system) => string;
  onChange: (option: system) => void;
  className?: string;
}

const Dropdown: FC<props> = (props) => {
  let { label, options, className, getLabel, onChange } = props;
  const [expanded, setExpanded] = useState(false);
  const [state, setState] = useState<system>();

  return (
    <div className={`${className ? className : "w-80"}`}>
      <div className='pb-3 pl-1 text-xl text-gray-300'>{label}</div>
      <div className='grid gap-2 relative'>
        <div
          className={`p-6 w-full h-max flex justify-between 
          rounded-lg bg-slate-800 hover:bg-slate-600 cursor-pointer`}
          onClick={() => setExpanded(!expanded)}
        >
          {state ? (
            <div className='text-white font-medium'>{getLabel(state)}</div>
          ) : (
            <div>&nbsp;</div>
          )}
          {expanded ? <ChevronUp /> : <ChevronDown />}
        </div>
        {expanded && (
          <div className='p-2 w-full overflow-auto h-60 grid grid-cols-1 rounded-lg bg-slate-700 absolute translate-y-[80px] z-10'>
            {options.map((item) => (
              <div
                key={getLabel(item)}
                className='p-4 rounded-lg hover:bg-gray-200/60 text-white hover:text-black hover:font-semibold cursor-pointer'
                onClick={() => {
                  setState(item);
                  onChange(item);
                  setExpanded(false);
                }}
              >
                {getLabel(item)}
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default Dropdown;
