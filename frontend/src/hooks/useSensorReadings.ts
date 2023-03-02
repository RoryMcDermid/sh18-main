import axios from "axios";
import { useEffect, useState } from "react";

const useSensorReadings = ({
  selectedSensors,
  startDate,
  endDate,
}: selection) => {
  const [sensorReading, setSensorReading] = useState<(string | number)[][]>([]);
  let sensorIDs = selectedSensors.join(",");
  const loadSensorReadings = () => {
    axios({
      method: "GET",
      url: `${
        import.meta.env.VITE_API
      }/sensors/${sensorIDs}/compare-and-display?startDate=${startDate}&endDate=${endDate}`,
    })
      .then((response: { data: [] }) => {
        console.log("GET SENSOR READING SUCCESS", response);
        setSensorReading(response.data);
      })
      .catch((error: { response: { data: { error: any } } }) => {
        console.log("GET SENSORS ERROR", error.response.data.error);
      });
  };

  useEffect(() => {
    loadSensorReadings();
  }, []);

  return sensorReading;
};

export default useSensorReadings;
