import { FC, useState } from "react";

interface props {
  label: string;
  items: string[];
  disableItems: number[];
  handleSelection: (n: number) => void;
}

const ButtonGroup: FC<props> = ({
  label,
  items,
  handleSelection,
  disableItems,
}) => {
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
      <div className='pb-3 pl-1 text-xl text-gray-300'>{label}</div>
      <div className='w-full inline-flex justify-between' role='group'>
        {items.map((item, i) => (
          <button
            key={i}
            className={`px-5 py-3 w-24 text-center text-lg font-semibold rounded-lg ${
              i === clickedId && "py-2.5 border-2 border-orange-500"
            } ${
              !disableItems.includes(i + 1)
                ? "text-gray-600 bg-gray-400"
                : "text-white bg-slate-800 hover:bg-slate-600"
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
