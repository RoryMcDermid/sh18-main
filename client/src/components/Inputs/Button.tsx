import { FC } from "react";

interface props {
  isDisabled?: boolean;
  text: string;
  handleClick?: () => void;
  classes?: string;
}

const Button: FC<props> = ({ text, handleClick, isDisabled, classes }) => {
  return (
    <>
      <button
        className={`px-5 py-3 w-full text-xl font-semibold rounded-lg
        ${classes ?? "w-32"}
        ${
          isDisabled
            ? "text-gray-600 bg-gray-400"
            : "text-white bg-orange-500 hover:bg-orange-600"
        }`}
        disabled={isDisabled}
        onClick={handleClick}
      >
        {text}
      </button>
    </>
  );
};

export default Button;
