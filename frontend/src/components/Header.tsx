import { FC } from "react";
import { Link } from "react-router-dom";
import { Button } from ".";

const Header: FC = () => {
  return (
    <>
      <header className='mx-20 flex h-[15vh] items-center justify-between'>
        <Link to='/'>
          <h1 className='animated-underline relative text-center text-4xl text-white'>
            Moxie Energy
          </h1>
        </Link>
        <div className='flex gap-10'>
          <Link to='/compare'>
            <Button text='Compare' className='w-40' />
          </Link>
          <Link to='/forecast'>
            <Button text='Forecast' className='w-40' />
          </Link>
        </div>
      </header>
    </>
  );
};

export default Header;
