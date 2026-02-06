import { useState, useEffect } from 'react'
import Dashboard from './Dashboard.tsx'

function App() {
  const [offline, setOffline] = useState(false)

  useEffect(() => {
    // Stub offline detection
    setOffline(!navigator.onLine)
  }, [])

  return (
    <div>
      {offline && <div>OFFLINE – using cached data</div>}
      <Dashboard />
    </div>
  )
}

export default App