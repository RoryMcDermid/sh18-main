import { FC } from "react";
import React from "react";
import { Button } from "../components/Inputs";
import { Link } from "react-router-dom";

const LandingScreen: FC = () => {
  return (
    <div>
      <div className='squares w-full mx-auto grid grid-cols-2 gap-10'>
        <div className='col-span-1 flex flex-col items-center'>
          <div className='border-2 border-white w-1/2 h-96 m-20'>
            <div className='mb-4 h-16 flex justify-center text-center items-center text-xl text-white font-semibold'>
              Most Expensive Sensors
            </div>
          </div>
          <Link to='/compare'>
            <Button text='Compare Screen' className='w-40 ' />
          </Link>
        </div>
        <div className='col-span-1 flex flex-col items-center'>
          <div className='border-2 border-white w-1/2 h-96 m-20'>
            <div className='mb-4 h-16 flex justify-center text-center items-center text-xl text-white font-semibold'>
              Most Expensive Smart Meters
            </div>
          </div>
          <Link to='/forecast'>
            <Button text='Forecast Screen' className='w-40' />
          </Link>
        </div>
      </div>
    </div>
  );
};

export default LandingScreen;
