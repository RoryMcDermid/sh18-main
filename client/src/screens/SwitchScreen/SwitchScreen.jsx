import { useState } from "react";
import allData from "../../data/energyDataAllAMR.json";
import ContAreaChart from "../../components/AreaChart/ContAreaChart";

const SwitchScreen = () => {
  let mockData = [];
  for (let j = 0; j <= 22; j++) {
    mockData.push({
      id: `machine ${j + 1}`,
      data: allData[`serialNo${j}`],
    });
  }

  const [selectedSource, setSelectedSource] = useState("");

  const handleSelect = (item) => {
    console.log(`select data source ${item.id}`);
    setSelectedSource(item);
  };

  return (
    <>
      <div className='w-full h-screen grid grid-cols-5'>
        <div className='col-span-4 mt-40'>
          {selectedSource && (
            <ContAreaChart
              dataSource={selectedSource.data}
              dataKey='EnergyUsage'
              title='Energy Usage'
            />
          )}
        </div>
        <div className='overflow-auto'>
          <div className='bg-gray-200/60'>&nbsp;</div>
          <div className='col-span-1 bg-gray-800'>
            {mockData.map((item) => (
              <div
                key={item.id}
                className={`m-2 p-3 rounded-lg ${
                  item.id == selectedSource.id
                    ? "text-red-600 font-bold"
                    : "text-white"
                } 
                hover:bg-gray-200/60 hover:font-semibold cursor-pointer`}
                onClick={() => handleSelect(item)}
              >
                {item.id}
              </div>
            ))}
          </div>
          <div className='bg-gray-200/60'>&nbsp;</div>
        </div>
      </div>
    </>
  );
};

export default SwitchScreen;
