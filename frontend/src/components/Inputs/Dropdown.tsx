import { FC, useState } from "react";
import { ChevronUp, ChevronDown } from "../SVGs";

interface props {
  label: string;
  options: string[];
  onChange: (option: string) => void;
  className?: string;
}

const Dropdown: FC<props> = (props) => {
  let { label, options, className, onChange } = props;
  const [expanded, setExpanded] = useState(false);
  const [state, setState] = useState("");

  return (
    <div className={`${className ? className : "w-80"}`}>
      <div className='pb-3 pl-1 text-xl text-slate-300'>{label}</div>
      <div className='relative grid gap-2'>
        <div
          className={`flex h-max w-full cursor-pointer justify-between 
          rounded-lg bg-slate-800 p-6 hover:bg-slate-600`}
          onClick={() => setExpanded(!expanded)}
        >
          {state ? (
            <div className='font-medium text-white'>{state}</div>
          ) : (
            <div>&nbsp;</div>
          )}
          {expanded ? <ChevronUp /> : <ChevronDown />}
        </div>
        {expanded && (
          <div className='absolute z-10 grid max-h-60 min-h-max w-full translate-y-[80px] grid-cols-1 overflow-auto rounded-lg bg-slate-700 p-2'>
            {options.map((option) => (
              <div
                key={option}
                className='cursor-pointer rounded-lg p-4 text-white hover:bg-slate-200/60 hover:font-semibold hover:text-black'
                onClick={() => {
                  setState(option);
                  onChange(option);
                  setExpanded(false);
                }}
              >
                {option}
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default Dropdown;
