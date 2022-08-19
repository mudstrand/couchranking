import { Link, useLocation } from "react-router-dom"

const MediaDetails = () => {
    const location = useLocation()
    console.log("data: " + location.state.title)
    return (
        <media-detail-section>
            <h1>Media Details</h1>
            <br />
            <table>
              <tbody>
              <tr>
                <td>
                  <img alt={location.state.title} src={location.state.poster}
            width="200" height="300" />
                </td>
                <td>
                  <p>Year: {location.state.year}</p>
                  <p>Rated: {location.state.rated}</p>
                  { location.state.streaming_source && 
                    <p>Source: {location.state.streaming_source}</p>
                  }
                </td>
              </tr>
              <tr>
                  <td colSpan="2">
                    <p>Cast: {location.state.actors}</p>
                  </td>
              </tr>
              </tbody>
            </table>
            <br />
            <p>Details on currently selected media</p>
            <br />
            <p>{location.state.plot}</p>
            <br />
            <div className="flexGrow">
                <Link to="/media">Media</Link>
            </div>
        </media-detail-section>
    )
}

export default MediaDetails