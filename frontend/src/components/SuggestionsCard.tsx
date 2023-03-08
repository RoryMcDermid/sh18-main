import { FC } from "react";

interface props {
  suggestionData: string[];
}

const SuggestionsCard: FC<props> = ({ suggestionData }) => {
  const getSuggestions = (data: string[]) => {
    return data;
  };
  const suggestions = getSuggestions(suggestionData).slice(1);

  const getBorderColor = (suggestion: string) => {
    if (suggestion.includes("high or low")) {
      return "border-slate-500";
    }
    if (suggestion.split(" ").includes("low")) {
      return "border-lime-600";
    }
    if (suggestion.split(" ").includes("high")) {
      return "border-red-600";
    }
    return "border-slate-500";
  };

  return (
    <>
      <ul
        className='flex h-max w-full flex-col justify-between gap-5 rounded-lg bg-slate-400 px-4 -mt-2 py-6'
      >
        {suggestions.map((suggestion, i) => (
          <li
            className={`rounded-lg border-4 px-3 py-2 text-sm ${getBorderColor(
              suggestion
            )}`}
            key={i}
          >
            {suggestion}
          </li>
        ))}
      </ul>
    </>
  );
};

export default SuggestionsCard;
