import { FC } from "react";

interface props {
  suggestionData: string[];
}

const SuggestionsCard: FC<props> = ({ suggestionData }) => {
  const getSuggestions = (data: string[]) => {
    return ["a", "b", "c"];
  };
  const suggestions = getSuggestions(suggestionData);

  return (
    <>
      <div>
        {suggestions.map((suggestion, i) => (
          <div key={i}>{suggestion}</div>
        ))}
      </div>
    </>
  );
};

export default SuggestionsCard;
