import { useState } from "react";
import { RoundedButton } from "./components/RoundedButton";

export function HomePage() {
  const [count, setCount] = useState(0);
  const [input, setInput] = useState("");

  function handleClick() {
    setCount((old) => { return old + 1 });
  }



  return (
    <div>
      <p>{count}</p>
      <p>{count}</p>

      <h1 id="count">{count}</h1>
      <button onClick={handleClick}>{count}</button>
      <p>{count}</p>
      <div>
        <label>
          My input
          <input type="text" value={input} onChange={(e) => setInput(e.target.value)}/>
        </label>

      </div>
      <button onClick={() => {
        console.log(input)
      }}>Save</button>
    </div>
  )
}


