import React, { useState, useEffect } from 'react';
import Media from './components/Media';
import MediaAdd from './components/MediaAdd';
import MediaDetails from './components/MediaDetails';
import Register from './components/Register';
import Login from './components/Login';
import Home from './components/Home';
import Layout from './components/Layout';
import Editor from './components/Editor';
import Admin from './components/Admin';
import Missing from './components/Missing';
import Unauthorized from './components/Unauthorized';
import Lounge from './components/Lounge';
import LinkPage from './components/LinkPage';
import RequireAuth from './components/RequireAuth';
import { Routes, Route } from 'react-router-dom';

const ROLES = {
  'User': 2003,
  'Editor': 1995,
  'Admin': 1998
}

function App() {
  // const [data, setData] = useState([{}])

  // useEffect(() => {
  //   fetch("/media").then(
  //     res => res.json()
  //   ).then(
  //     data => {
  //       setData(data)
  //       console.log(data)
  //     }
  //   )
  // }, [])

  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        {/* public routes */}
        <Route path="login" element={<Login />} />
        <Route path="register" element={<Register />} />
        <Route path="linkpage" element={<LinkPage />} />
        <Route path="unauthorized" element={<Unauthorized />} />

        {/* these routes are protected */}
        <Route element={<RequireAuth />}>
          <Route path="media-add" element={<MediaAdd />} />          
          <Route path="media-details" element={<MediaDetails />} />          
          <Route path="media" element={<Media />} />
          <Route path="/" element={<Home />} />
          <Route path="editor" element={<Editor />} />
          <Route path="admin" element={<Admin />} />
          <Route path="lounge" element={<Lounge />} />
        </Route>

        {/* catch all */}
        <Route path="*" element={<Missing />} />
      </Route>
    </Routes>
  )

  // return (
  //   <div align="center">
  //     <MyTable media={data} width="4" />
  //   </div>
  // )
  // return (
  //   <main className="App">
  //     {/* <MyTable media={data} width="4" /> */}
  //     {/* <Register /> */}
  //     <Login />
  //   </main>
  // );
}

export default App