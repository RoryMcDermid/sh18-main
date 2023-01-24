const getAveragePrice = (wholesalePrice: wholesalePriceResponse[]) => {
  let totalPrice = 0;

  wholesalePrice.forEach((pricePoint: wholesalePriceResponse) => {
    totalPrice += pricePoint["Overall"];
  });

  const totalPricePoints = wholesalePrice.length;

  return Math.ceil(totalPrice / totalPricePoints);
};

const getPeakWholesalePrices = (wholesalePrice: wholesalePriceResponse[]) => {
  const averagePrice = getAveragePrice(wholesalePrice);
  let filterwholesaleprice = wholesalePrice.map((item) => {
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
