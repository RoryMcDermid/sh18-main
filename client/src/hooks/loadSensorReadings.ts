import axios from "axios";
import { useState, useEffect, useCallback } from "react";

const loadSensorReadingData = (sensorIds: string): [any[][], () => void] => {
  const [sensorReading, setSensorReading] = useState<any[][]>([]);

  const loadSensorReading = useCallback(() => {
    axios({
      method: "GET",
      url: `${import.meta.env.VITE_API}/systems/2542/sensors/${sensorIds}`,
    })
      .then((response: { data: [] }) => {
        console.log("GET SENSOR READING SUCCESS", response);
        setSensorReading(response.data);
      })
      .catch((error: { response: { data: { error: any } } }) => {
        console.log("GET SENSORS ERROR", error.response.data.error);
      });
  }, [sensorIds]);

  return [sensorReading, loadSensorReading];
};

export default loadSensorReadingData;
