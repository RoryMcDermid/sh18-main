import { Route, Routes } from "react-router-dom";
import { Header } from "./components";
import { CompareScreen } from "./screens";
import FindingsScreen from "./screens/FindingsScreen";

function App() {
  return (
    <>
      <Header />
      <Routes>
        <Route path='/compare' element={<CompareScreen />} />
        <Route path='/findings' element={<FindingsScreen />} />
      </Routes>
    </>
  );
}

export default App;
