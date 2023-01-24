const getValidIntervals = (startDateString: string, endDateString: string) => {
  const startDate = new Date(startDateString);
  const endDate = new Date(endDateString);
  const diff = endDate.valueOf() - startDate.valueOf();
  const diffInDays = diff / (1000 * 60 * 60 * 24);

  if (diffInDays >= 28) return [4];
  else if (diffInDays >= 7) return [3, 4];
  else if (diffInDays >= 2) return [2, 3, 4];
  else return [1, 2, 3, 4];
};

export default getValidIntervals;
