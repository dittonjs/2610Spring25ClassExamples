import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import { createBrowserRouter, RouterProvider } from 'react-router';
import { Layout } from './Layout.jsx';
import { AppSubpage } from './AppSubpage.jsx';


const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    children: [
      {
        path: "info",
        element: <h2>I am on the info page</h2>,
      },
      {
        path: "app",
        element: <App />
      }
    ]
  },
]);

createRoot(document.getElementById('root')).render(
  <RouterProvider
    router={router}
  />,
)
