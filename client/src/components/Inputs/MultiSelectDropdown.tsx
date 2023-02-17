import { FC, useEffect, useState } from "react";
import { ChevronUp, ChevronDown } from "../SVGs";

interface props {
  label: string;
  items: string[];
  state: string[];
  setState: (n: string[]) => void;
  className?: string;
}

const MultiSelectDropdown: FC<props> = (props) => {
  let { label, items, state, setState, className } = props;
  const [expanded, setExpanded] = useState(false);
  const [allSelected, setAllSelected] = useState(false);

  const handleOption = (option: string) => {
    if (!state.includes(option)) {
      setState([...state, option]);
    } else {
      let newState = state.filter((item) => {
        return item != option;
      });
      setState(newState);
    }
  };

  const selectAll = () => {
    if (!allSelected) {
      setAllSelected(true);
      setState(items);
    } else {
      setAllSelected(false);
      setState([]);
    }
  };

  useEffect(() => {
    if (state.length != items.length) {
      setAllSelected(false);
    }
  }, [state]);

  return (
    <div className={`${className ?? "w-80"}`}>
      <div className='pb-3 pl-1 text-xl text-gray-300'>{label}</div>
      <div className='grid gap-2 relative'>
        <div
          className={`p-6 w-full h-max flex justify-between 
        rounded-lg bg-slate-800 hover:bg-slate-600 cursor-pointer`}
          onClick={() => setExpanded(!expanded)}
        >
          <p className='text-white font-medium'>{state.join(", ")}</p>
          {expanded ? <ChevronUp /> : <ChevronDown />}
        </div>
        {expanded && (
          <div className='p-2 w-full grid grid-cols-1 rounded-lg bg-slate-700 overflow-auto min-h-max max-h-72 absolute translate-y-[76px] z-10'>
            {items && (
              <div className='p-2 flex items-center'>
                <div
                  className='px-4 py-2 text-white bg-orange-500 hover:bg-orange-600 rounded-md cursor-pointer'
                  onClick={() => selectAll()}
                >
                  {!allSelected ? "Select all" : "Deselect all"}
                </div>
              </div>
            )}

            {items.map((item, i) => (
              <div
                key={i}
                className={`p-4 rounded-lg cursor-pointer hover:bg-gray-200/60
                  ${
                    state.includes(item)
                      ? "text-amber-600 hover:text-orange-700 font-semibold"
                      : "text-white hover:text-black hover:font-semibold"
                  }`}
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

export default MultiSelectDropdown;
