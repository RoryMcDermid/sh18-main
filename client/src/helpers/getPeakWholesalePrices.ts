import { formatDate } from ".";

const getAveragePrice = (wholesalePrice: wholesalePriceResponse[]) => {
  let totalPrice = 0;

  wholesalePrice.forEach((pricePoint) => {
    totalPrice += pricePoint["Overall"];
  });

  return Math.ceil(totalPrice / wholesalePrice.length);
};

const getPeakWholesalePrices = (wholesalePrice: wholesalePriceResponse[]) => {
  const averagePrice = getAveragePrice(wholesalePrice);
  const filterWholesalePrice = wholesalePrice.map((item) => {
    if (item["Overall"] > averagePrice) {
      return item["Timestamp"];
    }
  });

  let expensiveTimes = [] as string[][];
  let timeslot = [] as string[];

  for (let i = 0; i < filterWholesalePrice.length; i++) {
    if (!filterWholesalePrice[i]) continue;

    if (!filterWholesalePrice[i - 1]) {
      timeslot.push(formatDate(filterWholesalePrice[i] as string));
    }
    if (!filterWholesalePrice[i + 1]) {
      timeslot.push(formatDate(filterWholesalePrice[i] as string));

      expensiveTimes.push(timeslot);
      timeslot = [];
    }
  }
  return expensiveTimes;
};

export default getPeakWholesalePrices;
