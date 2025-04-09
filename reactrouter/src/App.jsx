import { useState } from 'react'
import { Link, Outlet } from 'react-router'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <h1><Link to="myotherpage">Go here</Link></h1>
      <Outlet />
    </>
  )
}

export default App
