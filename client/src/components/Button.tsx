import { FC } from "react";

interface props {
  isDisabled?: boolean;
  text: string;
  handleClick: () => void;
}

const Button: FC<props> = ({ text, handleClick, isDisabled }) => {
  return (
    <>
      <button
        className={`px-5 py-3 w-max text-xl font-semibold ${
          isDisabled
            ? "text-gray-600 bg-gray-400"
            : "text-white bg-orange-500 hover:bg-orange-600"
        } rounded-lg`}
        onClick={handleClick}
        disabled={isDisabled}
      >
        {text}
      </button>
    </>
  );
};

export default Button;
