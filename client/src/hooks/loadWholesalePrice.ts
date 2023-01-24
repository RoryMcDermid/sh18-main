import { useEffect, useState } from "react";
import axios from "axios";
import { formatDateForHook } from "../helpers";

const loadWholesalePrice = (startDateString: string, endDateString: string) => {
  const startDate = formatDateForHook(startDateString);
  const endDate = formatDateForHook(endDateString);

  const [wholesaleprice, setWholesaleprice] = useState<
    wholesalePriceResponse[]
  >([]);

  const loadWholesalePriceAPI = () => {
    axios({
      method: "GET",
      url: `https://odegdcpnma.execute-api.eu-west-2.amazonaws.com/development/prices?dno=18&voltage=HV&start=${startDate}&end=${endDate}`,
    })
      .then(async (response) => {
        console.log("LOAD WHOLEPRICE SUCCESS", response.data);
        const wholesalericeData = response.data.data.data;
        setWholesaleprice(wholesalericeData);
      })
      .catch((error) => {
        console.log("LOAD WHOLEPRICE ERROR", error);
      });
  };

  useEffect(() => {
    loadWholesalePriceAPI();
  }, [startDate, endDate]);

  return wholesaleprice;
};

export default loadWholesalePrice;
