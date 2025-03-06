import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000", // Asegúrate de cambiar esto según tu API
});

// Interceptor para incluir el token en todas las solicitudes
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("token");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default api;
