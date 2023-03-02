import { useEffect, useState } from "react";
import axios from "axios";

const useForecastData = (sensorID: string) => {
  const [chartData, setChartData] = useState<energyReading[][]>([]);
  const [suggestionData, setSuggestionData] = useState<string[]>([]);

  const loadForecastData = async (sensorID: string) => {
    axios({
      method: "GET",
      url: `${import.meta.env.VITE_API}/sensors/${sensorID}/forcast`,
    })
      .then((response: { data: { chartData: []; suggestionData: [] } }) => {
        console.log("GET FORECAST DATA SUCCESS", response);
        const forecastData = response.data;

        setChartData(forecastData.chartData);
        setSuggestionData(forecastData.suggestionData);
      })
      .catch((error: { response: { data: { error: any } } }) => {
        console.log("GET FORECAST DATA ERROR", error.response.data.error);
        setChartData([]);
        setSuggestionData([]);
      });
  };

  useEffect(() => {
    if (sensorID) {
      loadForecastData(sensorID);
    }
  }, []);

  return { chartData, suggestionData };
};

export default useForecastData;
