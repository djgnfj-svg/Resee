import axios from 'axios';

// Django API Base URL
const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/', // Django 서버 URL
});

export default api;
