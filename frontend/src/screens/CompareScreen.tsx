import { FC, useEffect, useState } from "react";
import { Link } from "react-router-dom";
import {
  Button,
  ButtonGroup,
  DatePicker,
  Dropdown,
  MultiSelectDropdown,
} from "../components/Inputs/.";
import { BarChart, MultiLineChart } from "../components";
import { getValidIntervals } from "../helpers";
import { loadSensorReadingData, loadSystems, useSensors } from "../hooks";
import Loading from 'react-loading';
import { toast } from 'react-toastify';

interface props {
  peakPriceTimes: string[][];
}

const CompareScreen: FC<props> = ({ peakPriceTimes }) => {

  const [formSelection, setFormSelection] = useState({
    selectedSensors: [] as string[],
    startDate: "",
    endDate: "",
    interval: -1,
  });

  const { selectedSensors, startDate, endDate, interval } = formSelection;

  const { systems } = loadSystems();
  const [selectedSystem, setSelectedSystem] = useState<system | null>(null);

  const { sensors } = useSensors(selectedSystem);

  const sensorReading = loadSensorReadingData({
    selectedSensors: selectedSensors,
    startDate: startDate,
    endDate: endDate,
    interval: interval,
  });

  const disableButton = !(
    selectedSensors.length > 0 &&
    startDate !== "" &&
    endDate !== "" &&
    interval >= 1 &&
    interval <= 4
  );

  const [currentChartType, setCurrentChartType] = useState(true);
  const [chartReady, setChartReady] = useState(false);
  const handleChartError = () => {
    setChartReady(false);
    toast.error('Failed to load chart.');
  };

  useEffect(() => {
    console.table(formSelection);
    setFormSelection({
      selectedSensors: [] as string[],
      startDate: "",
      endDate: "",
      interval: -1,
    });
  }, []);

  return (
      <>
        <div style={{ display: "flex", height: "97vh", width: "97vw"  }}>
          <div style={{ width: "65%" , marginRight: "30px", display: "flex", height: "100%"}}>
            {currentChartType && chartReady ?  (
                <MultiLineChart
                    headerRow={["", ...selectedSensors]}
                    data={sensorReading}
                    peakPriceTimes={peakPriceTimes}
                />
            ): (
        <Loading type="spin" color="#000" height={50} width={50} />
      )}
            {!currentChartType && chartReady ? (
                <BarChart
                    headerRow={["", ...selectedSensors]}
                    data={sensorReading}
                    peakPriceTimes={peakPriceTimes}
                />
            ): (
        <Loading type="spin" color="#000" height={50} width={50} />
      )}
          </div>
          <div style={{ width: "30%", height: "100%"}}>
            <div className='flex flex-col gap-5 w-[33rem]'>
              <Dropdown
              label='Select a system:'
              options={systems}
              onChange={(item) => setSelectedSystem(item)}
              className='w-full'
              getLabel={(system) => system.SYSTEM_NAME}
              />
              <MultiSelectDropdown
                  label='Select sensors:'
                  items={sensors}
                  state={selectedSensors}
                  setState={(e) =>
                      setFormSelection({...formSelection, selectedSensors: e,})
              }
                  className='w-full'
              />

              <div className='flex gap-10'>
                <DatePicker
                    label='Select a start date:'
                    state={startDate}
                    setState={(e) =>
                        setFormSelection({...formSelection, startDate: e.target.value})}
                />
                <DatePicker
                    label='Select an end date:'
                    state={endDate}
                    setState={(e) =>
                        setFormSelection({...formSelection, endDate: e.target.value,})}
                />
              </div>
              <ButtonGroup
                  label='Select sensor reading interval:'
                  items={["15m", "1h", "4h", "1d"]}
                  handleSelection={(i) =>
                      setFormSelection({...formSelection, interval: i,})}
                  disableItems={getValidIntervals(startDate, endDate)}
              />
              <div className="flex justify-between">
                <Button
                    text={currentChartType ? "Bar Chart" : "Line Chart"}
                    handleClick={() => setCurrentChartType(!currentChartType)}
                />
                <Link to='/compare'>
                  <Button text='Enter' isDisabled={disableButton} />
                </Link>
              </div>
            </div>
          </div>
        </div>
      </>
  );
};

export default CompareScreen;
