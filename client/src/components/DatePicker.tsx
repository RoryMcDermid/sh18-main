import { FC } from "react";

interface props {
  label: string;
  state: string;
  setState: (e: React.ChangeEvent<HTMLInputElement>) => void;
  classes?: string;
}

const DatePicker: FC<props> = ({ label, classes, state, setState }) => {
  return (
    <>
      <div className={`${classes ?? "w-80"}`}>
        <div className='pb-3 pl-1 text-xl text-gray-300'>{label}</div>
        <input
          className='p-6 w-full text-white rounded-lg bg-slate-800 hover:bg-slate-600 cursor-pointer'
          type='date'
          defaultValue={state}
          onChange={(e) => setState(e)}
        />
      </div>
    </>
  );
};

export default DatePicker;
