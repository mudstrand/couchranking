import { Link } from "react-router-dom"
import React, { useState, useEffect } from 'react';


function MediaAdd() {
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

  let createTable = () => {
    let media = data
    let table_width = 4

    let table = []
    let children = []
    for (let i = 0; i < media.length; i++) {
      let current_media = media[i]
      // let refid = "http://localhost:8000/media/" + current_media.id

      children.push(<td>
        <Link to="/media-details" state={current_media}>
          <img alt={current_media.title} src={current_media.poster}
            width="200" height="300" />
        </Link>
      </td>)

      let x = i + 1
      if ((x % table_width === 0) || (x === media.length)) {
        table.push(<tr key={x}>{children}</tr>)
        children = []
      }
    }
    console.log("table:" + table)
    return table
  }

  return (
    <media-section>
      <table>
        <tbody>
          {/* {this.table} */}
          {/* {this.createTable(data)} */}
          { createTable(data) }
        </tbody>
      </table>
    </media-section>)
}

export default MediaAdd;