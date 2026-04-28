from pydantic import BaseModel

class paciente(BaseModel):
    id_paciente : int
    nombre_paciente : str
    tipo_acceso : str
    estado : str