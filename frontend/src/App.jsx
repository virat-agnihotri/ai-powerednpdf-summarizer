import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  return (
    <div>
      <h1>{count}</h1>
      <button onClick={()=>setCount(count+1)}>Add to Count</button>
    </div>
  )
}

export default App
