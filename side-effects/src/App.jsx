import { useState } from "react"
import { useEffect } from "react"
import { KeyLogger } from "./keylogger"

function App() {
  const [breedsApiResponse , setBreedsApiResponse] = useState(null)
  const [imageApiResponse , setImageApiResponse] = useState(null)
  const [breed, setBreed] = useState("")
  const [useKeyLogger, setUseKeyLogger] = useState(false)



  useEffect(() => {
    fetch("https://dog.ceo/api/breeds/list/all")
      .then((res) => res.json())
      .then((data) => {
        // console.log(data)
        setBreedsApiResponse(data)
        const breeds = Object.keys(data.message)
        setBreed(breeds[0])
      })
  }, [])

  useEffect(() => {
    if (breed !== "") {
      fetch(`https://dog.ceo/api/breed/${breed}/images/random`)
        .then((res) => res.json())
        .then((data) => {
          setImageApiResponse(data)
        })
    }

  }, [breed])

  if (breedsApiResponse === null) {
    return <div>Loading...</div>
  }


  return (
    <div>
      <div>
        <input type="checkbox" checked={useKeyLogger} onChange={e => setUseKeyLogger(old => !old)}/>
      </div>
      {
        useKeyLogger && <KeyLogger />
      }

      <div>
        <select value={breed} onChange={(e) => setBreed(e.target.value)}>
          {Object.keys(breedsApiResponse.message).map((breed) => (
            <option key={breed} value={breed}>
              {breed}
            </option>
          ))}
        </select>
      </div>
      <img src={imageApiResponse?.message} alt="dog" />

    </div>
  )
}

export default App
