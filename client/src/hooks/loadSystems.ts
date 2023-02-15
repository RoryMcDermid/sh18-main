import { useEffect, useState } from "react";
import axios from "axios";

const loadSystems = () => {
  const [systems, setSystems] = useState<system[]>([]);

  useEffect(() => {
    const loadSystemData = () => {
      axios({
        method: "GET",
        url: `https://moxieenergydeploy-production.up.railway.app/systems`,
      })
        .then((response: { data: [] }) => {
          console.log("GET SYSTEMS SUCCESS", response);
          const systemArray = response.data;
          setSystems(
            systemArray.map(function (system) {
              return system;
            })
          );
        })
        .catch((error: { response: { data: { error: any } } }) => {
          console.log("GET SYSTEMS ERROR", error.response.data.error);
        });
    };

    loadSystemData();
  }, []);

  return { systems };
};

export default loadSystems;
