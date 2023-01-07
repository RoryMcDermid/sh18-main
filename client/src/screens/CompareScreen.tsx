import { FC, useState } from "react";
import testData from "../data/testData.json";
import Dropdown from "../components/Dropdown";
import Header from "../components/Header";
import MultiLineChart from "../components/Charts/MultiAreaChart";

import allTheData from "../data/myData";

let allTheDataForRealsies = [
  allTheData.t1,
  allTheData.t2,
  allTheData.t3,
  allTheData.t4,
];

const generateHeaderRow: (sensors: energyReadingArray[]) => string[] = (
  sensors
) => {
  return Array(sensors.length + 1).fill(" ");
};

const newData: (number | string)[][] = [
  generateHeaderRow(allTheDataForRealsies),
];
for (let i = 0; i < allTheDataForRealsies[0].length; i++) {
  let x_axis = allTheDataForRealsies[0][i].DATE_OF_RECORD;
  newData.push([
    x_axis,
    allTheDataForRealsies[0][i].VALUE,
    allTheDataForRealsies[1][i].VALUE,
    allTheDataForRealsies[2][i].VALUE,
    allTheDataForRealsies[3][i].VALUE,
  ]);
}

const CompareScreen: FC = () => {
  const [a, setA] = useState("");
  const [b, setB] = useState("");
  const dates = ["m1", "m2", "m3", "m4", "m5"];
  const sensors = ["2233", "2232", "2231", "2230", "2229"];
  return (
    <>
      <Header />
      <div className='h-[85vh] flex flex-row'>
        <div className='basis-9/12'>
          <MultiLineChart dataSource={newData} />
          <div className='flex justify-end px-10 py-5'>
            <button className='px-5 py-3 text-xl text-white font-semibold bg-slate-800 rounded-lg'>
              Bar Chart
            </button>
          </div>
        </div>
        <div className='pt-10 basis-3/12 flex flex-col gap-10 items-center'>
          <Dropdown
            label={"Select a time period: "}
            state={a}
            setState={setA}
            items={dates}
          />
          <Dropdown
            label={"Select a sensor:"}
            state={b}
            setState={setB}
            items={sensors}
          />
        </div>
      </div>
    </>
  );
};

export default CompareScreen;
