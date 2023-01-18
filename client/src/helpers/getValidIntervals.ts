const getValidIntervals: (
  startDateString: string,
  endDateString: string
) => number[] = (startDateString, endDateString) => {
  let startDate = new Date(startDateString);
  let endDate = new Date(endDateString);
  const diff = endDate.valueOf() - startDate.valueOf();
  const diffInDays = diff / (1000 * 60 * 60 * 24);

  let disableItems = [];
  if (diffInDays >= 28) disableItems = [4];
  else if (diffInDays >= 7) disableItems = [3, 4];
  else if (diffInDays >= 2) disableItems = [2, 3, 4];
  else disableItems = [1, 2, 3, 4];

  return disableItems;
};

export default getValidIntervals;
