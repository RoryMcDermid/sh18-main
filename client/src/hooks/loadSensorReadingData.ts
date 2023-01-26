import axios from "axios";
import { useEffect, useState } from "react";

const loadSensorReadingData = ({
  selectedSensors,
  startDate,
  endDate,
  interval,
}: selection) => {
  const [sensorReading, setSensorReading] = useState<energyReading[][]>([]);
  let sensorIDs = selectedSensors.join(",");
  const loadSensorReading = () => {
    axios({
      method: "GET",
      url: `${
        import.meta.env.VITE_API
      }/systems/2542/sensors/${sensorIDs}?startDate=${startDate}&endDate=${endDate}&interval=${interval}`,
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
    loadSensorReading();
  }, []);

  return sensorReading;
};

export default loadSensorReadingData;
