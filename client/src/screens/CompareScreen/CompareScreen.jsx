import { useState } from "react";
import { ReactComponent as CloseIcon } from "../../assets/close.svg";
import TripleAreaChart from "../../components/AreaChart/TripleAreaChart";

import allData from "../../data/energyDataAllAMR.json";
import emptyData from "../../data/emptyData.json";
import allStatusData from "../../data/building_ExpStatus.json";
import allPriceData from "../../data/priceData.json";

const CompareScreen = () => {
  // load AMR data
  let AMRdata = [];
  for (let j = 0; j <= 22; j++) {
    AMRdata.push({
      id: `building ${j + 1}`,
      data: allData[`serialNo${j}`],
      status: allStatusData[`serialNo${j}`],
    });
  }

  const [dataSource1, setDataSource1] = useState(emptyData);
  const [dataSource2, setDataSource2] = useState(emptyData);

  const handleColor = (item) => {
    if (item.id == dataSource1.id) return "text-[#ff0066] font-bold";
    if (item.id == dataSource2.id) return "text-[#0066ff] font-bold";
    else return "text-white";
  };

  const handleSelect = (newItem) => {
    if (dataSource1 == emptyData) {
      setDataSource1(newItem);
    } else if (dataSource2 == emptyData) {
      setDataSource2(newItem);
    }
  };

  const handleClose = (item) => {
    if (item.id == dataSource1.id) {
      setDataSource1(emptyData);
    } else if (item.id == dataSource2.id) {
      setDataSource2(emptyData);
    }
  };

  const handleClick = (item) => {
    if (![dataSource1.id, dataSource2.id].includes(item.id)) {
      handleSelect(item);
    } else {
      handleClose(item);
    }
  };

  return (
    <div className='w-full h-screen grid grid-cols-5'>
      <div className='col-span-4 mt-40'>
        <TripleAreaChart
          priceDataSource={allPriceData.priceData}
          dataSource1={dataSource1.data}
          dataKey1='EnergyUsage'
          dataSource2={dataSource2.data}
          dataKey2='EnergyUsage'
          title='Energy Usage'
          status1={dataSource1.status}
          status2={dataSource2.status}
        />
      </div>
      <div className='overflow-auto bg-gray-800'>
        <div className='col-span-1 '>
          {AMRdata.map((item) => (
            <div
              key={item.id}
              className={`m-2 p-3 flex justify-between items-center rounded-lg
                ${handleColor(
                  item
                )} cursor-pointer hover:bg-gray-200/60 hover:font-semibold`}
              onClick={() => handleClick(item)}
            >
              {item.id}
              {[dataSource1.id, dataSource2.id].includes(item.id) && (
                <CloseIcon />
              )}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default CompareScreen;
