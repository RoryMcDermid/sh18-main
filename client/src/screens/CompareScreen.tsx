import { FC, useState } from "react";
import MultiAreaChart from "../components/MultiAreaChart";
import testData from "../data/testData.json";
import Dropdown from "../components/Dropdown";
import Header from "../components/Header";

const CompareScreen: FC = () => {
  const [a, setA] = useState("hello");
  const machines = ["m1", "m2", "m3", "m4", "m5"];
  return (
    <>
      <Header />
      <div className='h-[85vh] flex flex-row'>
        <div className='basis-9/12'>
          <MultiAreaChart dataSource={testData} dataKey={"VALUE"} title={" "} />
        </div>
        <div className='pt-10 basis-3/12 flex flex-col gap-10 items-center'>
          <Dropdown
            label={"Date & Time: "}
            state={a}
            setState={setA}
            sensors={machines}
          />
          <Dropdown
            label={"Select a sensor:"}
            state={a}
            setState={setA}
            sensors={machines}
          />
        </div>
      </div>
    </>
  );
};

export default CompareScreen;
