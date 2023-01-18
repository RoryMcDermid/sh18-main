import { FC } from "react";

interface props {
  label: string;
  datetime: string;
  setDatetime: React.Dispatch<React.SetStateAction<string>>;
  classes?: string;
}

const DatePicker: FC<props> = ({ label, classes, datetime, setDatetime }) => {
  return (
    <>
      <div className={`${classes ?? "w-80"}`}>
        <div className='pb-3 pl-1 text-xl text-gray-300'>{label}</div>
        <input
          className='p-6 w-full text-white rounded-lg bg-slate-800 hover:bg-slate-600 cursor-pointer'
          type='date'
          id='start'
          defaultValue={datetime}
          onChange={(e) => setDatetime(e.target.value)}
        />
      </div>
    </>
  );
};

export default DatePicker;
