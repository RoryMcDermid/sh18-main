const generateHeaderRow: (sensors: energyReadingArray[]) => string[] = (
  sensors
) => {
  return Array(sensors.length + 1).fill(" ");
};

const formatChartData: (sensorData: energyReadingArray[]) => formattedData = (
  sensorData
) => {
  const newData: formattedData = [generateHeaderRow(sensorData)];
  for (let i = 0; i < sensorData[0].length; i++) {
    newData.push([
      sensorData[0][i].DATE_OF_RECORD,
      sensorData[0][i].VALUE,
      sensorData[1][i].VALUE,
      sensorData[2][i].VALUE,
      sensorData[3][i].VALUE,
    ]);
  }
  return newData;
};

export default formatChartData;
