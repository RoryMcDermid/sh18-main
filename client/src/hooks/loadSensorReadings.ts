import axios from "axios";
import { useState, useEffect } from "react";

const useLoadSensorReadingData = (sensorId: string) => {
  const [sensorReading, setSensorReading] = useState([]);

  useEffect(() => {
    const loadSensorReading = () => {
      axios({
        method: "GET",
        url: `${import.meta.env.VITE_API}/systems/2542/sensors/${sensorId}`,
      })
        .then((response: { data: [] }) => {
          console.log("GET SENSOR READING SUCCESS", response);
          setSensorReading(response.data);
        })
        .catch((error: { response: { data: { error: any } } }) => {
          console.log("GET SENSORS ERROR", error.response.data.error);
        });
    };
    loadSensorReading();
  }, []);

  return sensorReading;
};

export default useLoadSensorReadingData;
