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
      <div className={`${className ?? "w-48"}`}>
        <div className='pb-3 pl-1 text-xl text-slate-300'>{label}</div>
        <input
          className='w-full cursor-pointer rounded-lg bg-slate-800 p-6 text-white hover:bg-slate-600'
          type='date'
          value={state}
          onChange={(e) => setState(e)}
        />
      </div>
    </>
  );
};

export default DatePicker;
