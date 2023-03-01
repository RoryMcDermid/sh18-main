import { FC } from "react";
import { Link } from "react-router-dom";

const Header: FC = () => {
  return (
    <>
      <header className='mx-20 h-[15vh] flex justify-center items-center'>
        <Link to='/landing'>
          <div className='text-4xl text-white text-center'>Moxie Energy</div>
        </Link>
      </header>
    </>
  );
};

export default Header;
