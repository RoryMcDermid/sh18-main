import { FC } from "react";

interface props {
  label: string;
  state: string;
  setState: (e: React.ChangeEvent<HTMLInputElement>) => void;
  className?: string;
}

const DatePicker: FC<props> = (props) => {
  let { label, className, state, setState } = props;
  return (
    <>
      <div className={`${className ?? "w-80"}`}>
        <div className='pb-3 pl-1 text-xl text-gray-300'>{label}</div>
        <input
          className='p-6 w-full text-white rounded-lg bg-slate-800 hover:bg-slate-600 cursor-pointer'
          type='date'
          value={state}
          onChange={(e) => setState(e)}
        />
      </div>
    </>
  );
};

export default DatePicker;
