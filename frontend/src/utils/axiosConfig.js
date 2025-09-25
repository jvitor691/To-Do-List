import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  timeout: 10000,
});


export const fetcher = async () => {
  const { data } = await api.get("/tasks");
  return data;
};


export const criar = async (payload) => {
  const { data } = await api.post("/tasks", payload);
  return data;
};


export const atualizar = async (id, payload) => {
  const { data } = await api.put(`/tasks/${id}`, payload);
  return data;
};


export const deletar = async (id) => {
  await api.delete(`/tasks/${id}`);
  return true;
};


export const patch = async (id, novoStatus) => {
  const { data } = await api.patch(`/tasks/${id}/status`, null, {
    params: { status: novoStatus },
  });
  return data;
};
