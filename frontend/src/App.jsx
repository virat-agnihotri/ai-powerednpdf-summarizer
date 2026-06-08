import { useState } from 'react'
import './App.css'
import Student from './student.jsx'

function App() {
  const [count, setCount] = useState(0)

  return (
  <>
    <Student name="virat"/>
    <div className='navbar'>
      hello
    </div>
    </>
  )
}

export default App
