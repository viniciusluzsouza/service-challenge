import axios from "axios";
import { getToken } from "./auth"

const api = axios.create({
  baseURL: "http://localhost:5010"
});

api.interceptors.request.use(async config => {
    const token = getToken();
    if (token) {
        config.headers.Authorization = `bearer ${token}`;
    }
  return config;
});

export default api;
