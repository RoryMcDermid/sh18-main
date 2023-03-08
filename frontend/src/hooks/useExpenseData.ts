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
        let now = new Date(Date.now());
        Object.assign(expenseData, {"date": now});
        setLocalStorage("expensive_data", JSON.stringify(expenseData))
      })
      .catch((error: { response: { data: { error: any } } }) => {
        console.log("GET EXPENSE DATA ERROR", error.response.data.error);
        setExpensiveSensors([]);
        setExpensiveSystems([]);
      });
  };

  const hasItBeenADay = (startDate: Date, endDate: Date) => {
      let tomorrow = new Date()
      tomorrow.setDate(startDate.getDate() + 1)
      if (endDate >= tomorrow) {
        return true
      }
      return false
  }

  const getLocalStorageValues = async () => {
      const expenseDataString = await JSON.parse(localStorage.getItem('expensive_data')!);
      if (expenseDataString !== null) {
        const expenseData = JSON.parse(expenseDataString);
        let now = new Date(Date.now());
        let loadDate = new Date(expenseData.date);
        if (hasItBeenADay(loadDate, now)) {
          loadExpenseData();
        } else {
        setExpensiveSensors(expenseData.sensors);
        setExpensiveSystems(expenseData.systems);
        }
      }
  }
  
  useEffect(() => {
    if (localStorage.getItem("expensive_data") !== null) {
      getLocalStorageValues()
    } else {
      loadExpenseData();
    }
  }, []);

  return { expensiveSystems, expensiveSensors };
};

export default useExpenseData;
