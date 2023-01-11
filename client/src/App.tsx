import { Route, Routes } from "react-router-dom";
import CompareScreen from "./screens/CompareScreen";
import SystemSelectScreen from "./screens/SystemSelectScreen";

function App() {
  return (
    <Routes>
      <Route path='/' element={<SystemSelectScreen />} />
      <Route path='/compare' element={<CompareScreen />} />
    </Routes>
  );
}

export default App;
