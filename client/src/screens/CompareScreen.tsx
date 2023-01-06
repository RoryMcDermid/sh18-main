import { FC, useState } from "react";
import MultiAreaChart from "../components/Charts/MultiAreaChart";
import testData from "../data/testData.json";
import Dropdown from "../components/Dropdown";
import Header from "../components/Header";

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
          <MultiAreaChart dataSource={testData} dataKey={"VALUE"} title={" "} />
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
