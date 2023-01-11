import { FC, useState } from "react";
import { Link } from "react-router-dom";
import { Button, Dropdown, Header } from "../components";
import { allSystemData } from "../data";

const SystemSelectScreen: FC = () => {
  const [selectedSystem, setSelectedSystem] = useState<string>("");
  const disable = !(selectedSystem !== "");
  return (
    <>
      <Header />
      <div className='mx-20 flex flex-row items-end gap-10'>
        <Dropdown
          label='Select System:'
          items={allSystemData}
          state={selectedSystem}
          setState={setSelectedSystem}
          classes='w-[40rem]'
        />
        <Link className='my-3' to='/compare'>
          <Button isDisabled={disable} text='Enter' handleClick={() => {}} />
        </Link>
      </div>
    </>
  );
};

export default SystemSelectScreen;
