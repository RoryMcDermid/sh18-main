interface props {
  headerRow: string[];
  sensorData: energyReadingArray[];
}

const formatChartData: (a: props) => formattedData = ({
  headerRow,
  sensorData,
}) => {
  const newData: formattedData = [headerRow];
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
