import { useState } from "react"
import { useEffect } from "react"

function App() {
  console.log("Hello, world")
  const [breedsApiResponse , setBreedsApiResponse] = useState(null)
  const [imageApiResponse , setImageApiResponse] = useState(null)
  const [breed, setBreed] = useState("")


  useEffect(() => {
    fetch("https://dog.ceo/api/breeds/list/all")
      .then((res) => res.json())
      .then((data) => {
        console.log(data)
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

  useEffect(() => {
    const keydown = (e) => {
      console.log(breed)
      console.log(e.key)
    }
    window.addEventListener("keydown", keydown);

    return () => {
      window.removeEventListener("keydown", keydown);
    }
  }, [breed])

  if (breedsApiResponse === null) {
    return <div>Loading...</div>
  }

  return (
    <div>
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
