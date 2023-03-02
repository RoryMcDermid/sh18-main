import { FC } from "react";
import { Link } from "react-router-dom";

const Header: FC = () => {
  return (
    <>
      <header className='mx-20 flex h-[15vh] items-center justify-center'>
        <Link to='/'>
          <div className='animated-underline relative text-center text-4xl text-white'>
            Moxie Energy
          </div>
        </Link>
      </header>
    </>
  );
};

export default Header;
