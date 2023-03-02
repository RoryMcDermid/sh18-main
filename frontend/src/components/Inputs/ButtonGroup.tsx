import { FC, useState } from "react";

interface props {
  label: string;
  items: string[];
  disableItems: number[];
  handleSelection: (n: number) => void;
}

const ButtonGroup: FC<props> = (props) => {
  let { label, items, handleSelection, disableItems } = props;
  const [clickedId, setClickedId] = useState(-1);

  const handleClick = (
    _: React.MouseEvent<HTMLButtonElement, MouseEvent>,
    i: number
  ) => {
    setClickedId(i);
    handleSelection(i + 1);
  };

  return (
    <div>
      <div className='pb-3 pl-1 text-xl text-slate-300'>{label}</div>
      <div className='inline-flex w-full justify-between' role='group'>
        {items.map((item, i) => (
          <button
            key={i}
            className={`w-24 rounded-lg px-5 py-3 text-center text-lg font-semibold ${
              i === clickedId && "border-2 border-orange-500 py-2.5"
            } ${
              !disableItems.includes(i + 1)
                ? "bg-slate-400 text-slate-600"
                : "bg-slate-800 text-white hover:bg-slate-600"
            }`}
            onClick={(e) => handleClick(e, i)}
            disabled={!disableItems.includes(i + 1)}
          >
            {item}
          </button>
        ))}
      </div>
    </div>
  );
};

export default ButtonGroup;
