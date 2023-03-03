import { useEffect, useState } from "react";
import axios from "axios";

const useSensors = (systemID: number | undefined) => {
  const [sensors, setSensors] = useState<string[]>([]);

  const loadSensorsData = async (system: string) => {
    axios({
      method: "GET",
      url: `${import.meta.env.VITE_API}/systems/${system}/sensors`,
    })
      .then((response: { data: [] }) => {
        console.log("GET SENSORS SUCCESS", response);
        const sensorsArray = response.data;
        setSensors(
          sensorsArray.map(function (sensor) {
            return sensor[0];
          })
        );
      })
      .catch((error: { response: { data: { error: any } } }) => {
        console.log("GET SENSORS ERROR", error.response.data.error);
        setSensors([]);
      });
  };

  useEffect(() => {
    if (systemID) {
      loadSensorsData(systemID.toString());
    }
  }, [systemID]);

  return { sensors };
};

export default useSensors;
