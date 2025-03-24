import { useState } from "react";

function App() {
  const [todoList, setTodoList] = useState([]);
  const [content, setContent] = useState("");
  console.log(todoList);
  return (
    <>
      <h1>Type your todo item</h1>
      <div>

        <input
          type="text"
          value={content}
          onChange={e => setContent(e.target.value)}
        />
        <button onClick={() => {
          const todo = {
            content,
            done: false,
          }

          setContent("");
          setTodoList(oldTodo => [...oldTodo, todo]);
        }}>Save</button>
      </div>
      {
        todoList.map(todo => (
          <div key={todo.content}>
            {todo.content}
            <input
              type="checkbox"
              checked={todo.done}
              onChange={() => {
                setTodoList(oldList => {
                  const newTodo = {...todo, done: !todo.done};
                  const index = oldList.indexOf(todo);
                  const oldList = [...oldList];
                  oldList[index] = newTodo;
                  return oldList;
                })
              }}
            />
          </div>
        ))
      }
    </>
  )
}

export default App
