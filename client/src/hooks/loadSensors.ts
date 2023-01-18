import { useEffect, useState } from "react";
import axios from "axios";

const loadSensors = () => {
  const [sensors, setSensors] = useState([]);

  useEffect(() => {
    const loadSensorsData = () => {
      axios({
        method: "GET",
        url: `${import.meta.env.VITE_API}/systems/2542/sensors`,
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
        });
    };

    loadSensorsData();
  }, []);

  return sensors;
};

export default loadSensors;
