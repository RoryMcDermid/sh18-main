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
        className='flex h-max w-full flex-col justify-between gap-7 rounded-lg bg-slate-400 px-6 
          py-8'
      >
        {suggestions.map((suggestion, i) => (
          <div
            className={`rounded-lg border-4 px-3 py-2 ${
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
