import { Route, Routes } from "react-router-dom";
import { Header } from "./components";
import { SystemSelectScreen, CompareScreen } from "./screens";

function App() {
  return (
    <>
      <Header />
      <Routes>
        <Route path='/' element={<SystemSelectScreen />} />
        <Route path='/compare' element={<CompareScreen />} />
      </Routes>
    </>
  );
}

export default App;
