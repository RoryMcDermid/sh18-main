const findAveragePrice = (wholesaleprice: any[]) => {
  let totalPrice = 0;
  const addToTotal = (pricePoint: any) => {
    totalPrice += pricePoint["Overall"];
  };
  wholesaleprice.forEach(addToTotal);

  let totalPricePoints = wholesaleprice.length;

  return Math.ceil(totalPrice / totalPricePoints);
};

const getPeakWholesalePrices = (wholesaleprice: any[]) => {
  let averagePrice = findAveragePrice(wholesaleprice);
  let filterwholesaleprice = wholesaleprice.map((item) => {
    if (item.Overall > averagePrice) {
      return item.Timestamp;
    }
  });
  let expensiveTimes: any[] = [];
  let timeslot = Array(2);
  for (let i = 0; i < filterwholesaleprice.length; i++) {
    if (
      filterwholesaleprice[i] != undefined &&
      filterwholesaleprice[i - 1] === undefined
    ) {
      timeslot[0] = filterwholesaleprice[i];
    }
    if (
      filterwholesaleprice[i] != undefined &&
      filterwholesaleprice[i + 1] === undefined
    ) {
      timeslot[1] = filterwholesaleprice[i];
      expensiveTimes.push(timeslot);
      timeslot = Array(2);
    }
  }
  return expensiveTimes;
};

export default getPeakWholesalePrices;
