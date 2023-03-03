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
      <div className='pb-3 pl-1 text-xl text-slate-300'>{label}</div>
      <div className='relative grid gap-2'>
        <div
          className={`flex h-max w-full cursor-pointer justify-between 
        rounded-lg bg-slate-800 p-6 hover:bg-slate-600`}
          onClick={() => setExpanded(!expanded)}
        >
          <p className='font-medium text-white'>{state.join(", ")}</p>
          {expanded ? <ChevronUp /> : <ChevronDown />}
        </div>
        {expanded && (
          <div className='absolute z-10 grid max-h-72 min-h-max w-full translate-y-[76px] grid-cols-1 overflow-auto rounded-lg bg-slate-700 p-2'>
            {items && (
              <div className='flex items-center p-2'>
                <div
                  className='cursor-pointer rounded-md bg-orange-500 px-4 py-2 text-white hover:bg-orange-600'
                  onClick={() => selectAll()}
                >
                  {!allSelected ? "Select all" : "Deselect all"}
                </div>
              </div>
            )}

            {items.map((item, i) => (
              <div
                key={i}
                className={`cursor-pointer rounded-lg p-4 hover:bg-slate-200/60
                  ${
                    state.includes(item)
                      ? "font-semibold text-amber-600 hover:text-orange-700"
                      : "text-white hover:font-semibold hover:text-black"
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
