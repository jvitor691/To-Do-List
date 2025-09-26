import { useEffect, useState } from 'react';
import '../App.css';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import AddIcon from '@mui/icons-material/Add';
import FilterListIcon from '@mui/icons-material/FilterList';
import FilterModal from '../components/FilterModal';
import {
  fetcher,
  criar,
  atualizar,
  deletar,
  patch
} from '../utils/axiosConfig';

const Home = () => {
  const [task, setTask] = useState({ titulo: '', descricao: '', status: 'pendente' });
  const [taskList, setTaskList] = useState([]);

  const [editId, setEditId] = useState(null);         
  const [filter, setFilter] = useState('todas');      
  const [openFilter, setOpenFilter] = useState(false);

  const [loading, setLoading] = useState(false);
  const [err, setErr] = useState('');

  
  useEffect(() => {
    (async () => {
      try {
        setLoading(true);
        const data = await fetcher(); 
        setTaskList(Array.isArray(data) ? data : []);
      } catch (e) {
        console.error(e);
        setErr('Falha ao carregar tarefas.');
      } finally {
        setLoading(false);
      }
    })();
  }, []);

  const Preenchimento = (e) => {
    const { name, value } = e.target;
    setTask((prev) => ({ ...prev, [name]: value }));
  };

  const AdicionarOuSalvar = async () => {
    if (!task.titulo.trim()) {
      alert('Por favor, preencha todos os campos.');
      return;
    }

    try {
      setLoading(true);
      setErr('');

      if (editId == null) {
        const nova = await criar({
          titulo: task.titulo,
          descricao: task.descricao,
          status: task.status || 'pendente',
        });
        setTaskList((prev) => [nova, ...prev]);
      } else {
        const atualizado = await atualizar(editId, {
          titulo: task.titulo,
          descricao: task.descricao,
          status: task.status || 'pendente',
        });
        setTaskList((prev) => prev.map((t) => (t.id === editId ? atualizado : t)));
        setEditId(null);
      }

      setTask({ titulo: '', descricao: '', status: 'pendente' });
    } catch (e) {
      console.error(e);
      setErr('Erro ao salvar tarefa.');
    } finally {
      setLoading(false);
    }
  };

  
  const Editar = (index) => {
    const t = visibleTasks[index]; 
    if (!t) return;
    setTask({ titulo: t.titulo, descricao: t.descricao, status: t.status });
    setEditId(t.id);
  };

  const Excluir = async (index) => {
    const t = visibleTasks[index];
    if (!t) return;

    if (!window.confirm(`Excluir a tarefa "${t.titulo}"?`)) return;

    const snapshot = [...taskList];
    try {
      setTaskList((prev) => prev.filter((item) => item.id !== t.id));
      await deletar(t.id);
    } catch (e) {
      console.error(e);
      setErr('Erro ao excluir tarefa.');

      setTaskList(snapshot);
    }
  };

  const alterarStatus = async (index, novoStatus) => {
  const t = visibleTasks[index];
  if (!t) return;

  try {
    setLoading(true);
    setErr('');
    const atualizado = await patch(t.id, { status: novoStatus }); 
    setTaskList((prev) => prev.map((item) => (item.id === t.id ? atualizado : item)));
  } catch (e) {
    console.error(e);
    setErr('Erro ao atualizar status.');
  } finally {
    setLoading(false);
  }
};
  const visibleTasks = taskList.filter((t) =>
    filter === 'todas' ? true : t.status === filter
  );

  return (
    <section className="card">
      <h1>To-do List</h1>
      <div className="actions">
        <button className="filtro" onClick={() => setOpenFilter(true)}>
          <FilterListIcon /> Filtro: {filter}
        </button>
      </div>

      <div className="inputs">
        <label>Título</label>
        <input
          type="text"
          name="titulo"
          value={task.titulo}
          onChange={Preenchimento}
          placeholder="Adicione uma task..."
        />

        <label>Descrição</label>
        <input
          type="text"
          name="descricao"
          value={task.descricao}
          onChange={Preenchimento}
          placeholder="Adicione uma descrição..."
        />

        <button onClick={AdicionarOuSalvar}>
          <AddIcon /> {editId == null ? 'Adicionar' : 'Salvar'}
        </button>
      </div>

      {loading && <p>Carregando...</p>}
      {!!err && <p style={{ color: 'red' }}>{err}</p>}

      {visibleTasks.length === 0 ? (
        <p className="empty-message">Nenhuma tarefa para este filtro</p>
      ) : (
        visibleTasks.map((item, index) => (
          <div key={item.id ?? index} className="task">
            <div className="info">
              <h4>{item.titulo}</h4>
              <p>{item.descricao}</p>
            </div>

            <select
              name="status"
              value={item.status}
              onChange={(e) => alterarStatus(index, e.target.value)}
            >
              <option value="pendente">Pendente</option>
              <option value="concluida">Concluído</option>
            </select>

            <div className="botoes">
              <button className="editar" onClick={() => Editar(index)}>
                <EditIcon />
              </button>
              <button className="excluir" onClick={() => Excluir(index)}>
                <DeleteIcon />
              </button>
            </div>
          </div>
        ))
      )}
      {openFilter && (
        <FilterModal
          open={openFilter}
          onClose={() => setOpenFilter(false)}
          value={filter}
          onChange={(val) => setFilter(val)}
        />
      )}
    </section>
  );
};

export default Home;
