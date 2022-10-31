import { useState } from "react";
import { ReactComponent as CloseIcon } from "../../assets/close.svg";

const CompareScreen = () => {
  let mockData = [];
  for (let j = 0; j < 22; j++) {
    mockData.push({
      id: `machine ${j + 1}`,
      data: "hello",
    });
  }

  const [selectedData, setSelectedData] = useState([]);

  const containsObject = (list, obj) => {
    for (let i = 0; i < list.length; i++) {
      if (list[i].id === obj.id) {
        return true;
      }
    }
    return false;
  };

  const handleSelect = (newItem) => {
    if (containsObject(selectedData, newItem)) return;
    setSelectedData((oldData) => [...oldData, newItem]);
  };

  const handleClose = (item) => {
    setSelectedData((oldData) => {
      return oldData.filter((oldItem) => {
        return item.id !== oldItem.id;
      });
    });
  };

  return (
    <>
      <div className='w-full h-screen grid grid-cols-5'>
        <div className='col-span-4 mt-52'></div>
        <div className='overflow-auto'>
          <div className='col-span-1 bg-gray-800'>
            {selectedData.map((item) => (
              <div
                key={item.id}
                className={`m-2 p-3 flex justify-between items-center
                rounded-lg text-white border-2 border-gray-200/60 cursor-pointer
                hover:font-semibold hover:border-red-700 hover:text-red-500`}
                onClick={() => handleClose(item)}
              >
                <p>{item.id}</p>
                <CloseIcon className='h-5 w-5' />
              </div>
            ))}
          </div>
          <div className='bg-gray-200/60'>&nbsp;</div>
          <div className='col-span-1 bg-gray-800'>
            {mockData.map((item) => (
              <div
                key={item.id}
                className='m-2 p-3 rounded-lg text-white hover:bg-gray-200/60 hover:font-semibold cursor-pointer'
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

export default CompareScreen;
