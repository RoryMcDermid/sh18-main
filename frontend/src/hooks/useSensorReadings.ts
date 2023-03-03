import axios from "axios";
import { useCallback, useEffect, useState } from "react";

const useSensorReadings = ({
  selectedSensors,
  startDate,
  endDate,
}: selection) => {

  const [sensorReadings, setSensorReadings] = useState([])


  const getSensorReadings = useCallback(({selectedSensors, startDate, endDate}:selection) => {

    let sensorIDs = selectedSensors.join(",");
    console.table({sensorIDs, startDate, endDate})
    axios({
      method: "GET",
      url: `${
        import.meta.env.VITE_API
      }/sensors/${sensorIDs}/compare-and-display?startDate=${startDate}&endDate=${endDate}`,
      
    })
      .then((response: { data: [] }) => {
        console.log("GET SENSOR READING SUCCESS", response);
        setSensorReadings(response.data)
              })
      .catch((error: { response: { data: { error: any } } }) => {
        console.log("GET SENSORS ERROR", error.response.data.error);
      });
      
  }, [selectedSensors, startDate, endDate]);

  

  return {sensorReadings, getSensorReadings}
};

export default useSensorReadings;
