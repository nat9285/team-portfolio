import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import axios from 'axios' /*importamos axios, de la librería de la cual ya descargamos, para aplicar el paquete */
import { useEffect } from 'react'

function App() {

  useEffect()
  axios.get

  return (
    <div className='my-5 text-center'>

      <div className='card mx-auto ' style={{maxWidth: '520px'}}>

        <div className='card-body'>

          <div className='d-flex gap-3 justify-content-center '>

              <a href="https://vitejs.dev" target="_blank">
                <img src={viteLogo} className="logo" alt="Vite logo" />
              </a>
              <a href="https://react.dev" target="_blank">
                <img src={reactLogo} className="logo react" alt="React logo" />
              </a>

          </div>

          <h1>Portfolio</h1>

          <div className="">

          </div>

        </div>
       
       </div>
     
    </div>
  )
}

export default App
