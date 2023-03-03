import { useEffect, useState } from "react";
import axios from "axios";

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
      })
      .catch((error: { response: { data: { error: any } } }) => {
        console.log("GET EXPENSE DATA ERROR", error.response.data.error);
        setExpensiveSensors([]);
        setExpensiveSystems([]);
      });
  };

  useEffect(() => {
    loadExpenseData();
  }, []);

  return { expensiveSystems, expensiveSensors };
};

export default useExpenseData;
