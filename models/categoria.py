from pydantic import BaseModel

class categoria(BaseModel):
    id_categoria : int
    nombre_categoria : str