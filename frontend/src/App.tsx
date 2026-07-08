import { useEffect, useState, } from 'react'
import api from './services/api'
import './App.css'
interface Exercise {
  id: number;
  name: string;
  muscle_group: string;
  description: string;
}
function App() {
  const [exercises, setExercises] = useState<Exercise[]>([]);

useEffect(() => {
  async function fetchExercises() {
    try {

      const response = await api.get("/api/exercises/");

      setExercises(response.data);

    } catch (error) {
      console.error("Failed to fetch exercises: ", error);
    }
  }

  fetchExercises();

}, []);
  return (
    
      <section id="center">
        
        <h1>Training Tracker Exercises</h1>

        {exercises.map((exercise) => (

          <div key={exercise.id}>

            <h2>{exercise.name}</h2>

            <p>Muscle Group:{" "} {exercise.muscle_group}</p>

            <p>{exercise.description}</p>
          </div>
        ))} 
        
      </section>

  
  );
}

export default App
