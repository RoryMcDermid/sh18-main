import { FC } from "react";
import useExpenseData from "../hooks/useExpenseData";

const LandingScreen: FC = () => {
  const { expensiveSensors, expensiveSystems } = useExpenseData();
  return (
    <div>
      <div className='mx-auto mt-20  flex flex-row justify-center gap-20'>
        <div className='w-1/4 rounded-lg bg-gray-800 p-8 shadow-lg'>
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
                <div className='flex w-full justify-between rounded-md bg-gray-700 py-3 px-6 transition-all duration-150 hover:scale-[1.01] hover:bg-gray-400 hover:text-black'>
                  <p>{system[0]}</p>
                  <p>£{system[1].toFixed(2)}</p>
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className='w-1/4 rounded-lg bg-gray-800 p-8 shadow-lg'>
          <h2 className='mb-8 h-max text-lg font-semibold text-slate-200 underline underline-offset-4'>
            Most Expensive Smart Meters
          </h2>
          <div className='flex flex-col gap-5'>
            {expensiveSensors.map((sensor, i) => (
              <div
                key={i}
                className='flex items-center gap-6 font-semibold text-slate-200'
              >
                <p>{i + 1}.</p>
                <div className='flex w-full justify-between rounded-md bg-gray-700 py-3 px-6 transition-all duration-150 hover:scale-[1.01] hover:bg-gray-400 hover:text-black'>
                  <p>{sensor[0]}</p>
                  <p>£{sensor[1].toFixed(2)}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default LandingScreen;
