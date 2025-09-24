import { use, useState } from 'react'
import '../App.css'
 import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import AddIcon from '@mui/icons-material/Add';

const Home = () => {
    
    const [task, setTask] = useState({titulo : "", descricao: "" ,completed: false});
    const [taskList, setTaskList] = useState([]); 
        
    
    
    return (
        <section className='card'>
            <h1>To-do List</h1>
            <div className='inputs'>
            <label>Titulo</label>
            <input type="text" placeholder="Adicione uma task..." />
            <label>Descrição</label>
            <input type="text" placeholder="Adicione uma task..." />
            <button><AddIcon />Adicionar</button>
            </div>
            <div className='task'>
                <div className='info'>
                <h4>Titulo</h4> 
                <p>Exemplo Lorem ipsum dolor sit amet consectetur, adipisicing elit. Culpa illum facilis omnis adipisci expedita inventore unde ut quam blanditiis architecto laboriosam sunt aspernatur, maiores exercitationem quibusdam at amet sit? Accusamus!</p>
                </div>
                <select name="status" id="status">
                     <option value="...">...</option>
                    <option value="pendente">Pendente</option>
                    <option value="concluido">Concluido</option>
                </select>
                
                <div className='botoes'>
                    <button className='editar'><EditIcon /></button>
                    <button className='excluir'><DeleteIcon /></button>
                </div>

            </div>
        </section>
    )
}
export default Home;