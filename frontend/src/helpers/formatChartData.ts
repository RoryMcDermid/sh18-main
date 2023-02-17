const formatChartData = (
  headerRow: string[],
  sensorData: energyReading[][]
) => {
  const newData = [] as (string | number)[][];
  newData.push(headerRow);
  if (sensorData.length > 0) {
    for (let i = 0; i < sensorData[0].length; i++) {
      newData.push([
        // TODO: change date format
        sensorData[0][i].DATE_OF_RECORD,
        ...sensorData.map((readingArray) => {
          return parseFloat(readingArray[i].VALUE as string);
        }),
      ]);
    }
  }
  return newData;
};

export default formatChartData;
