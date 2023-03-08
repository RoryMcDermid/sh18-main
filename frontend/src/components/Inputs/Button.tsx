import { FC } from "react";

interface props {
  isDisabled?: boolean;
  text: string;
  handleClick?: () => void;
  className?: string;
}

const Button: FC<props> = (props) => {
  let { text, handleClick, isDisabled, className } = props;
  return (
    <>
      <button
        className={`h-full rounded-lg px-5 py-3 text-xl font-semibold shadow-sm transition-all duration-200
        ${className ?? "w-32"}
        ${
          isDisabled
            ? "bg-slate-400 text-slate-600"
            : "bg-orange-500 text-white hover:scale-[1.02] hover:bg-orange-600"
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
