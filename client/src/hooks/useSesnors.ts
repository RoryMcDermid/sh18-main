import { useEffect, useState } from "react";
import axios from "axios";

const useSensors = (system: system | null) => {
  console.log(system);

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
            return sensor["SENSOR_ID"];
          })
        );
      })
      .catch((error: { response: { data: { error: any } } }) => {
        console.log("GET SENSORS ERROR", error.response.data.error);
        setSensors([]);
      });
  };

  useEffect(() => {
    if (system) {
      console.log(system);
      loadSensorsData(system.SYSTEM_ID.toString());
    }
  }, [system]);

  return { sensors };
};

export default useSensors;
