import { useEffect, useState, } from 'react'
import api from './services/api'
import './App.css'
interface Exercise {
  id: number;
  name: string;
  muscle_group: string;
}
function App() {
  const [exercises, setExercises] = useState<Exercise[]>([]);
  /*const [serverData, setServerData] = useState({
    message: "",
    status: "",
    version:"",
    developer: "",

  }
)*/
useEffect(() => {
  async function fetchServerData() {
    try {
      const response = await api.get("/api/exercises/");
      
      console.log(response);
      console.log(response.data);

      ///setServerData(response.data);
      setExercises(response.data);
    } catch (error) {
      console.error("Failed to contact backend:", error);
    }
  }

  fetchServerData();
}, []);
  return (
    
      <section id="center">
        <div>
          {/* <h1>{serverData.message}</h1> */}
          {/* <p>{serverData.status}</p> */}
          {/* <p>Version: {serverData.version}</p> */}
          {/* <p>Developer: {serverData.developer}</p> */}
          {/* <p>Exercises: {serverData.exercises}</p> */}
          <h1>Exercises</h1>
          {exercises.map((exercise) => (
            <div key={exercise.id}>
              <h2>{exercise.name}</h2>
              <p>Muscle Group: {exercise.muscle_group}</p>
          
        </div>
        ))}
        </div>
      </section>

  
  )
}

export default App
