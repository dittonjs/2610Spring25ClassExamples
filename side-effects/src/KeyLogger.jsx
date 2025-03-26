import { useEffect, useState } from "react";

export function KeyLogger() {
  const [pressedKeys, setPressedKeys] = useState(new Set());

  useEffect(() => {
    console.log("KeyLogger component mounted");
    const keydown = (e) => {
      console.log("keydown")
      setPressedKeys((prev) => new Set(prev).add(e.key));
    };

    const keyup = (e) => {
      console.log("keyup")
      setPressedKeys((prev) => {
        const newSet = new Set(prev);
        newSet.delete(e.key);
        return newSet;
      });
    };

    window.addEventListener("keydown", keydown);
    window.addEventListener("keyup", keyup);

    return () => {
      console.log("KeyLogger component unmounted");
      window.removeEventListener("keydown", keydown);
      window.removeEventListener("keyup", keyup);
    };
  }, [])

  return (
    <div>
      <h1>Pressed keys</h1>
      <ul>
        {[...pressedKeys].map((key) => (
          <li key={key}>{key}</li>
        ))}
      </ul>
    </div>
  );
}
