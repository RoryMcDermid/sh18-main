import { FC, useState } from "react";
import { ChevronUp, ChevronDown } from ".";

interface props {
  label: string;
  items: string[];
  state: string[];
  setState: (newValue: string[]) => void;
}

const Dropdown: FC<props> = ({ label, items, state, setState }) => {
  const [expanded, setExpanded] = useState(false);

  const handleOption = (option: string) => {
    const newState = state;
    newState.push(option);
    setState(newState);
  };

  return (
    <div>
      <div className="pb-3 pl-1 text-xl text-white">{label}</div>
      <div className="grid gap-2 relative">
        <div
          className={`p-6 w-80 h-max flex justify-between 
        rounded-lg bg-slate-800 hover:bg-slate-600 cursor-pointer`}
          onClick={() => setExpanded(!expanded)}
        >
          <p className="text-white font-medium">{state.join(", ")}</p>
          {expanded ? <Up /> : <Down />}
        </div>
        {expanded && (
          <div className="p-2 w-80 overflow-auto h-60 grid grid-cols-1 rounded-lg bg-slate-700 absolute translate-y-[80px] z-10">
            {items.map((item) => (
              <div
                key={item}
                className="p-4 rounded-lg hover:bg-gray-200/60 text-white hover:text-black hover:font-semibold cursor-pointer"
                onClick={() => {
                  handleOption(item);
                }}
              >
                {item}
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default Dropdown;
