import React, { useState, useEffect } from 'react'
import MyTable from './PosterTable'

function App() {
  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("/media").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])

  return (
    <div align="center">
      <MyTable media={data} width="4" />
    </div>
  )
}

export default App