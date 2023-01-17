import { useEffect, useState } from "react";
import axios from "axios";

export const loadWholesalePrice = (startDate: string, endDate: string) => {
  const [wholesaleprice, setWholesaleprice] = useState([]);

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
        console.log("LOAD WHOLEPRICE ERROR", error.response.data.error);
      });
  };

  useEffect(() => {
    loadWholesalePriceAPI();
  }, []);

  return wholesaleprice;
};
