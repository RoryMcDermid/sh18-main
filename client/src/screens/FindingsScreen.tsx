import { FC } from "react";

const FindingsScreen: FC = () => {
  const expensiveSystems: string[] = ["system1", "system2", "system3"];
  const variableSystems: string[] = ["system1", "system2", "system3"];
  const expensiveSensors: string[] = ["sensor1", "sensor2", "sensor3"];
  const variableSensors: string[] = ["sensor1", "sensor2", "sensor3"];

  return (
    <>
      <div className='mt-10 px-8 flex flex-row justify-evenly'>
        <div className='w-[16rem] flex flex-col gap-7'>
          <div className='mb-4 h-16 flex justify-center text-center items-center text-xl  text-orange-500 underline underline-offset-4 font-semibold'>
            Most Expensive Buildings
          </div>
          {expensiveSystems.map((system) => {
            return (
              <div className='py-3 px-5 bg-slate-500 rounded-lg text-white'>
                {system}
              </div>
            );
          })}
        </div>
        <div className='w-[16rem] flex flex-col gap-7'>
          <div className='mb-4 h-16 flex justify-center text-center items-center text-xl  text-orange-500 underline underline-offset-4 font-semibold'>
            Most Variable Buildings
          </div>
          {variableSystems.map((system) => {
            return (
              <div className='py-3 px-5 bg-slate-500 rounded-lg text-white'>
                {system}
              </div>
            );
          })}
        </div>
        <div className='w-[16rem] flex flex-col gap-7'>
          <div className='mb-4 h-16 flex justify-center text-center items-center text-xl  text-orange-500 underline underline-offset-4 font-semibold'>
            Most Expensive Smart Meters
          </div>
          {expensiveSensors.map((sensor) => {
            return (
              <div className='py-3 px-5 bg-slate-500 rounded-lg text-white'>
                {sensor}
              </div>
            );
          })}
        </div>
        <div className='w-[16rem] flex flex-col gap-7'>
          <div className='mb-4 h-16 flex justify-center text-center items-center text-xl  text-orange-500 underline underline-offset-4 font-semibold'>
            Most Variable Smart Meters
          </div>
          {variableSensors.map((sensor) => {
            return (
              <div className='py-3 px-5 bg-slate-500 rounded-lg text-white'>
                {sensor}
              </div>
            );
          })}
        </div>
      </div>
    </>
  );
};

export default FindingsScreen;
