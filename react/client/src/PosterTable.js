import React from 'react';

export default class MyTable extends React.Component {
  createTable = (props) => {
    let media = this.props.media
    let table_width = this.props.width

    let table = []
    let children = []
    for (let i = 0; i < media.length; i++) {
      let current_media = media[i]
      let refid = "http://localhost:8000/media/" + current_media.id

      children.push(<td><a href={refid}>
        <img alt={current_media.title} src={current_media.poster}
          width="200" height="300" /></a></td>)

      let x = i + 1
      if ((x % table_width === 0) || (x === media.length)) {
        table.push(<tr key={x}>{children}</tr>)
        children = []
      }
    }
    return table
  }

  render() {
    return (
      <table>
        <tbody>
          {this.createTable()}
        </tbody>
      </table>
    )
  }

}