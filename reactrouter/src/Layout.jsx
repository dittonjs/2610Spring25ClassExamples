import { Link, Outlet } from "react-router";

export function Layout() {
  return (
    <div>
      <header>
        <h1>My Application</h1>
        <Link to="/app">App</Link>
        <span> | </span>
        <Link to="/info">Info</Link>
      </header>
      <main>
        <h1>Before3</h1>
        <Outlet />
        <h1>After3</h1>
      </main>
      <footer>
        <p>© 2025 My Application</p>
      </footer>
    </div>
  )
}
