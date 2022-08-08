import React, { useState, useEffect } from 'react'

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
    <div>

        {(typeof data.map === 'undefined') ? (
            <p>Loading...</p>
        ) : (
            data.map((media, i) => (
                <p key={i}>{media.title}</p>
            ))
        )}
        
    </div>
  )
}

export default App