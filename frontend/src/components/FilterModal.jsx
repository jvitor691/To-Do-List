import {Dialog, DialogTitle, DialogContent, DialogActions,
  Button, RadioGroup, FormControlLabel, Radio} from '@mui/material';

export default function FilterModal({ open, onClose, value, onChange }) {
  return (
    <Dialog open={open} onClose={onClose} fullWidth maxWidth="xs">
      <DialogTitle>Filtrar tarefas</DialogTitle>
      <DialogContent dividers>
        <RadioGroup
          value={value}
          onChange={(e) => onChange(e.target.value)}
          name="task-filter"
        >
          <FormControlLabel value="todas" label="Todas" control={<Radio />} />
          <FormControlLabel value="pendente" label="Pendentes" control={<Radio />} />
          <FormControlLabel value="concluida" label="Concluídas" control={<Radio />} />
        </RadioGroup>
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose} variant="outlined">Fechar</Button>
        <Button onClick={onClose} variant="contained">Aplicar</Button>
      </DialogActions>
    </Dialog>
  );
}
