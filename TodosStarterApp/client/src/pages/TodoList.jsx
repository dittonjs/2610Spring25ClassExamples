import { useEffect, useState } from "react";
import { Link } from "react-router";
import { Todo } from "../components/Todo";

export function TodoList() {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    async function fetchTodos() {
      const response = await fetch("/todos/", {
        credentials: "same-origin",
        headers: {
          "Accept": "application/json",
        }
      });
      if (response.ok) {
        const {todos} = await response.json();
        setTodos(todos);
      }
    }
    fetchTodos();
  }, [])
  // This is a placeholder for the TodoList component
  return (
    <div>
      <Link to="/new">+ New Todo</Link>
      {
        todos.map(todo => (
          <Todo key={todo.id} todo={todo} />
        ))
      }
    </div>
  );
}
