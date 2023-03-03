import { FC } from "react";
import { Button } from "../components/Inputs";
import { Link } from "react-router-dom";
import useExpenseData from "../hooks/useExpenseData";

const LandingScreen: FC = () => {
  const { expensiveSensors, expensiveSystems } = useExpenseData();
  return (
    <div>
      <div className='squares mx-auto grid grid-cols-9 grid-rows-[9] gap-y-3'>
        <div className='col-span-2 col-start-3 row-span-3 row-start-1 rounded-lg bg-gray-800 p-8 shadow-lg'>
          <h2 className='mb-8 text-lg font-semibold text-slate-200 underline underline-offset-4'>
            Most Expensive Buildings
          </h2>
          <div className='flex flex-col gap-5'>
            {expensiveSystems.map((system, i) => (
              <div
                key={i}
                className='flex items-center gap-6 font-semibold text-slate-200'
              >
                <p>{i + 1}.</p>
                <button className='flex w-full justify-between rounded-md bg-gray-700 py-3 px-6 transition-all duration-150 hover:scale-[1.01] hover:bg-gray-400 hover:text-black'>
                  <p>{system[0]}</p>
                  <p>£{system[1].toFixed(2)}</p>
                </button>
              </div>
            ))}
          </div>
        </div>

        <div className='col-span-2 col-start-3 row-span-3 row-start-5  rounded-lg bg-gray-800 p-8 shadow-lg'>
          <h2 className='mb-8 text-lg font-semibold text-slate-200 underline underline-offset-4'>
            Most Expensive Smart Meters
          </h2>
          <div className='flex flex-col gap-5'>
            {expensiveSensors.map((sensor, i) => (
              <div
                key={i}
                className='flex items-center gap-6 font-semibold text-slate-200'
              >
                <p>{i + 1}.</p>
                <button className='flex w-full justify-between rounded-md bg-gray-700 py-3 px-6 transition-all duration-150 hover:scale-[1.01] hover:bg-gray-400 hover:text-black'>
                  <p>{sensor[0]}</p>
                  <p>£{sensor[1].toFixed(2)}</p>
                </button>
              </div>
            ))}
          </div>
        </div>
        <div className='col-span-2 col-start-5 row-span-1 row-start-2 ml-10 rounded-lg '>
          <Link to='/forecast'>
            <Button text='Forecast Screen' className='w-40' />
          </Link>
        </div>
        <div className='col-span-2 col-start-5 row-span-1 row-start-6 ml-10 rounded-lg '>
          <Link to='/compare'>
            <Button text='Compare Screen' className='w-40' />
          </Link>
        </div>
      </div>
    </div>
  );
};

export default LandingScreen;
