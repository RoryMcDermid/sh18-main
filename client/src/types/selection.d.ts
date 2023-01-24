type dateRange = {
  startDate: string;
  endDate: string;
};

interface selection {
  selectedSensors: string[];
  startDate: string;
  endDate: string;
  interval: number;
}
