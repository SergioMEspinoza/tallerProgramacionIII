from pydantic import BaseModel

class personal(BaseModel):
    id_personal : int
    nombre : str
    sexo : str
    edad : int
    id_usuario : int