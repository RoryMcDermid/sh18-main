import { FC } from "react";

interface props {
  text: string;
  handleClick: () => void;
}

const Button: FC<props> = ({ text, handleClick }) => {
  return (
    <>
      <button
        className='px-5 py-3 text-xl text-white font-semibold bg-orange-500 hover:bg-orange-600 rounded-lg'
        onClick={handleClick}
      >
        {text}
      </button>
    </>
  );
};

export default Button;
