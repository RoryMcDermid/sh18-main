import { useEffect, useState } from "react";
import axios from "axios";
import { setLocalStorage } from "../helpers";

const useExpenseData = () => {
  type expenseInfo = [string, number] & { length: 2 };

  const [expensiveSensors, setExpensiveSensors] = useState<expenseInfo[]>([]);
  const [expensiveSystems, setExpensiveSystems] = useState<expenseInfo[]>([]);

  const loadExpenseData = async () => {
    axios({
      method: "GET",
      url: `${import.meta.env.VITE_API}/expensive-systems-sensors`,
    })
      .then((response: { data: { systems: []; sensors: [] } }) => {
        console.log("GET EXPENSE DATA SUCCESS", response);
        const expenseData = response.data;
        setExpensiveSensors(expenseData.sensors);
        setExpensiveSystems(expenseData.systems);
        setLocalStorage("expensive_data", JSON.stringify(expenseData))
      })
      .catch((error: { response: { data: { error: any } } }) => {
        console.log("GET EXPENSE DATA ERROR", error.response.data.error);
        setExpensiveSensors([]);
        setExpensiveSystems([]);
      });
  };

  async function getValueFromLocalStorage() {
    const expenseDataString = await JSON.parse(localStorage.getItem('expensive_data')!);
    if (expenseDataString !== null) {
      const expenseData = JSON.parse(expenseDataString);
      setExpensiveSensors(expenseData.sensors);
      setExpensiveSystems(expenseData.systems);
    }
  }


  useEffect(() => {
    if (localStorage.getItem("expensive_data") !== null) {
      getValueFromLocalStorage()
    } else {
      loadExpenseData();
    }
  }, []);

  return { expensiveSystems, expensiveSensors };
};

export default useExpenseData;
