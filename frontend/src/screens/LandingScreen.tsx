import { FC } from "react";
import React from "react";
import { Button } from "../components/Inputs"
import { Link } from "react-router-dom";

const LandingScreen: FC = () => {

  return (
    <div>
      <div className="squares flex justify-between w-full mx-auto">
          <div className='border-2 border-white w-2/5 h-96 m-20'>
              <div className='mb-4 h-16 flex justify-center text-center items-center text-xl text-white font-semibold'>
                  Most Expensive Sensors
              </div>
          </div>
          <div className='border-2 border-white w-2/5 h-96 m-20'>
              <div className='mb-4 h-16 flex justify-center text-center items-center text-xl text-white font-semibold'>
                  Most Expensive Smart Meters
              </div>
          </div>
      </div>
        <div className="flex justify-between w-full mx-auto">
            <Link to="/compare">
                <Button
                    text="Compare Screen"
                    className="w-40 ml-80 "
                />
            </Link>
            <Link to="/forecast">
                <Button
                    text="Forecast Screen"
                    className="w-40 mr-80"
                />
            </Link>
        </div>
    </div>
  );
};

export default LandingScreen;
