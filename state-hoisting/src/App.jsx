import { useState } from 'react'
import './App.css'
import { Input } from './components/Input'

function App() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')

  function handleSubmit(e) {
    e.preventDefault();
    console.log('submit')
    console.log("Logging in with email" + email)
    console.log("Logging in with password" + password)
  }

  return (

      <div className='container'>
        <form className='form' onSubmit={handleSubmit}>
          <h2>Login</h2>
          <Input
            label="Password"
            type="password"
            value={password}
            onChange={e => setPassword(e.target.value)}
          />
          <Input
            label="Email"
            value={email}
            onChange={e => setEmail(e.target.value)}
          />
          <button className='button'>Login</button>
        </form>
      </div>

  )
}

export default App
