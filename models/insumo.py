from pydantic import BaseModel

class insumo(BaseModel):
    id_insumo : int
    nombre_insumo : str
    descripcion_insumo : str
    minimo_stock : int
    cantidad_stock : int
    estado : str
    id_categoria : int