import { FC, useState } from "react";
import { Link } from "react-router-dom";
import { Button, Dropdown, Header } from "../components";
import { formatDropdownData } from "../helpers";
import {
  findAveragePrice,
  getPeakWholesalePrices,
} from "../helpers/getPeakWholesalePrices";
import { loadSystems } from "../hooks";
import { loadWholesalePrice } from "../hooks/loadWholesalePrice";

const SystemSelectScreen: FC = () => {
  const sensorArray = loadSystems();
  const wholesaleprice = loadWholesalePrice("10-01-2023", "16-01-2023");
  const peaktimes = getPeakWholesalePrices(wholesaleprice);
  console.log(peaktimes);

  const [selectedSystem, setSelectedSystem] = useState<string>("");
  const disable = !(selectedSystem !== "");
  return (
    <>
      <Header />
      <div className="mx-20 flex flex-row items-end gap-10">
        <Dropdown
          label="Select System:"
          items={formatDropdownData(sensorArray)}
          state={selectedSystem}
          setState={setSelectedSystem}
          classes="w-[40rem]"
        />
        <Link className="my-3" to="/compare">
          <Button isDisabled={disable} text="Enter" handleClick={() => {}} />
        </Link>
      </div>
    </>
  );
};

export default SystemSelectScreen;
