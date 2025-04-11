import cookies from "js-cookie";
import { useState } from "react";
export function Todo({todo}) {
  const [completed, setCompleted] = useState(todo.completed);

  async function onCheckChange(e) {

    const response = await fetch(`/todos/${todo.id}/`, {
      method: "PUT",
      credentials: "same-origin",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": cookies.get("csrftoken")
      },
      body: JSON.stringify({
        completed: e.target.checked
      }),
    });
    if(response.ok) {
      setCompleted(!completed);
    }

  }
  return (
    <div>
      <h2>
        {todo.title}
        <input
          type='checkbox'
          checked={completed}
          onChange={onCheckChange}
        />
      </h2>
      <p>{todo.description}</p>
    </div>
  )
}
