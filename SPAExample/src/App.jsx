import { useState } from "react"
import { Home } from "./pages/Home";
import { Dashboard } from "./pages/Dashboard";
import { Settings } from "./pages/Settings";

function App() {
  const [count, setCount] = useState(0);
  const [page, setPage] = useState("home");

  let headerClass = "header";
  if (page === "home") {
    headerClass = "header lightblue";
  }

  let PageComponent;

  if (page === "home") {
    PageComponent = Home;
  }
  else if (page === "dashboard") {
    PageComponent = Dashboard;
  }
  else if (page === "settings") {
    PageComponent = Settings;
  } else {
    PageComponent = () => <div>Page not found</div>
  }

  return (
    <>
      <div className={headerClass}>
        <h1>Welcome to my app!</h1>
        <button onClick={() => setCount(c => c+1)}>{count}</button>
        <button onClick={() => setPage("home")}>Home</button>
        <button onClick={() => setPage("dashboard")}>Dashboard</button>
        <button onClick={() => setPage("settings")}>Settings</button>
        <button onClick={() => setPage("courses")}>Courses</button>
      </div>
      <PageComponent />
    </>
  )
}

export default App
