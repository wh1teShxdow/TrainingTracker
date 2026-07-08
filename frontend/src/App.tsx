import { useEffect, useState, } from 'react'
import api from './services/api'
import './App.css'

function App() {
  const [serverData, setServerData] = useState({
    message: "",
    status: "",
    version:"",
    developer: "",
    exercises: "",
  }
)
useEffect(() => {
  async function fetchServerData() {
    try {
      const response = await api.get("/");
      console.log(response);
      console.log(response.data);

      setServerData(response.data);
    } catch (error) {
      console.error("Failed to contact backend:", error);
    }
  }

  fetchServerData();
}, []);
  return (
    
      <section id="center">
        <div>
          <h1>{serverData.message}</h1>
          <p>{serverData.status}</p>
          <p>Version: {serverData.version}</p>
          <p>Developer: {serverData.developer}</p>
          <p>Exercises: {serverData.exercises}</p>
        </div>
      </section>

  
  )
}

export default App
