import { useEffect, useState } from "react";
import axios from "axios";

export const loadWholesalePrice = (startDate: string, endDate: string) => {
  const [wholesaleprice, setWholesaleprice] = useState([]);

  useEffect(() => {
    const loadWholesalePriceAPI = () => {
      axios({
        method: "GET",
        url: `https://odegdcpnma.execute-api.eu-west-2.amazonaws.com/development/prices?dno=18&voltage=HV&start=${startDate}&end=${endDate}`,
      })
        .then(async (response) => {
          console.log("LOAD WHOLEPRICE SUCCESS", response.data);
          const wholesalericeData = response.data.data.data.map(
            (reading: any) => {
              return {
                value: reading["Overall"],
                timestamp: reading["Timestamp"],
              };
            }
          );
          setWholesaleprice(wholesalericeData);
          console.log(wholesaleprice);
        })
        .catch((error) => {
          console.log("LOAD WHOLEPRICE ERROR", error.response.data.error);
        });
    };

    loadWholesalePriceAPI();
  }, []);

  return wholesaleprice;
};
