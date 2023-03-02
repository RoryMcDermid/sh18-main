import { useEffect, useState } from "react";
import axios from "axios";

const useSystems = () => {
  const [systems, setSystems] = useState<system[]>([]);

  const loadSystemData = () => {
    axios({
      method: "GET",
      url: `${import.meta.env.VITE_API}/systems`,
    })
      .then((response: { data: [] }) => {
        console.log("GET SYSTEMS SUCCESS", response);
        const systemArray = response.data;
        setSystems(
          systemArray.map((system) => {
            return system;
          })
        );
      })
      .catch((error: { response: { data: { error: any } } }) => {
        console.log("GET SYSTEMS ERROR", error.response.data.error);
      });
  };

  useEffect(() => {
    loadSystemData();
  }, []);

  return { systems };
};

export default useSystems;
