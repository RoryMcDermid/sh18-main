import { FC } from "react";

interface props {
  suggestionData: string[];
}

const SuggestionsCard: FC<props> = ({ suggestionData }) => {
  const getSuggestions = (data: string[]) => {
    return data;
  };
  const suggestions = getSuggestions(suggestionData);

  return (
    <>
      <div
        className='bg-slate-400 px-6 py-8 w-full h-max flex flex-col gap-7 justify-between 
          rounded-lg'
      >
        {suggestions.map((suggestion, i) => (
          <div
            className={`px-3 py-2 rounded-lg border-4 ${
              i % 2 == 0 ? "border-red-600" : "border-lime-600"
            }`}
            key={i}
          >
            {suggestion}
          </div>
        ))}
      </div>
    </>
  );
};

export default SuggestionsCard;
