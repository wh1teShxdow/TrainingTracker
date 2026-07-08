/**

 * TrainingTracker Frontend
 * File:
 * api.ts
 *
 * Purpose:
 * Configure Axios once for the entire application.
 
 */

import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

export default api;