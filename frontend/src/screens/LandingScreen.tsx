import { FC, useState } from "react";
import React from "react";
import { Button } from "../components/Inputs";
import { Link } from "react-router-dom";
import useExpenseData from "../hooks/useExpenseData";

const LandingScreen: FC = () => {
  const { expensiveSensors, expensiveSystems } = useExpenseData();
  return (
    <div>
      <div className='squares mx-auto grid w-full grid-cols-2 gap-10'>
        <div className='col-span-1 flex flex-col items-center'>
          <div className='m-20 h-96 w-1/2 border-2 border-white'>
            <div className='mb-4 flex h-16 items-center justify-center text-center text-xl font-semibold text-white'>
              Most Expensive Sensors
            </div>
            {expensiveSensors.map((sensor, i) => (
              <div key={i}>{sensor.at(0)}</div>
            ))}
          </div>
          <Link to='/compare'>
            <Button text='Compare Screen' className='w-40 ' />
          </Link>
        </div>
        <div className='col-span-1 flex flex-col items-center'>
          <div className='m-20 h-96 w-1/2 border-2 border-white'>
            <div className='mb-4 flex h-16 items-center justify-center text-center text-xl font-semibold text-white'>
              Most Expensive Smart Meters
            </div>
            {expensiveSystems.map((system, i) => (
              <div key={i}>{system.at(0)}</div>
            ))}
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
