import { time } from "console";

export const findAveragePrice = (wholesaleprice: any[]) => {
  let totalPrice = 0;
  function addToTotal(pricePoint: any) {
    totalPrice += pricePoint["Overall"];
  }
  wholesaleprice.forEach(addToTotal);

  let totalPricePoints = wholesaleprice.length;

  return Math.ceil(totalPrice / totalPricePoints);
};

export const getPeakWholesalePrices = (wholesaleprice: any[]) => {
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

export const convertTimeFormatForSensors = (wholesalePriceTime: string) => {
  // need to turn "19:00 11-01-2023" into "2023-01-11T19:00:00.000Z";
};
