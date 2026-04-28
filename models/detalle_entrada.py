from pydantic import BaseModel

class detalle_entrada(BaseModel):
    id_detalle_entrada : int
    id_entrada : int
    id_insumo : int
    cantidad : int