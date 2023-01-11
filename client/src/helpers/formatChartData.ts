interface props {
  headerRow: string[];
  sensorData: energyReadingArray[];
}

const formatChartData: (
  sensorData: energyReadingArray[]
) => formattedData | undefined = (sensorData) => {
  const newData: formattedData = [generateHeaderRow(sensorData)];
  if (sensorData.length > 0) {
    for (let i = 0; i < sensorData[0].length; i++) {
      newData.push([
        sensorData[0][i].DATE_OF_RECORD,
        ...sensorData.map((readingArray) => {
          return readingArray[i].VALUE;
        }),
      ]);
    }
  }
  return newData;
};

export default formatChartData;
