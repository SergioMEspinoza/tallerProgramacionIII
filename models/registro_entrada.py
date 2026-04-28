from pydantic import BaseModel
from datetime import datetime

class registro_entrada(BaseModel):
    id_entrada : int
    fecha_entrada : datetime
    id_usuario : int