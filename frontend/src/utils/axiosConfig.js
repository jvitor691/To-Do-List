import axios from "axios";

const baseURL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000';
console.log('API Base URL:', baseURL);

const api = axios.create({
  baseURL: baseURL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});


export const fetcher = async () => {
  const { data } = await api.get("/tasks");
  return data;
};


export const criar = async (payload) => {
  console.log('Criando task com payload:', payload);
  console.log('URL completa:', baseURL + '/tasks');
  try {
    const { data } = await api.post("/tasks", payload);
    console.log('Task criada com sucesso:', data);
    return data;
  } catch (error) {
    console.error('Erro ao criar task:', error);
    console.error('Response:', error.response?.data);
    throw error;
  }
};


export const atualizar = async (id, payload) => {
  const { data } = await api.put(`/tasks/${id}`, payload);
  return data;
};


export const deletar = async (id) => {
  await api.delete(`/tasks/${id}`);
  return true;
};


export const patch = async (id, body) => {
  const { data } = await api.patch(`/tasks/${id}/status`, body);
  return data;
};
