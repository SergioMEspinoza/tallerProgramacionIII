from pydantic import BaseModel
from datetime import datetime

class registro_salida(BaseModel):
    id_salida : int
    fecha_salida : datetime
    id_usuario : int
    id_paciente : int