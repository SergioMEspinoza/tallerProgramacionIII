from pydantic import BaseModel

class detalle_salida(BaseModel):
    id_detalle_salida : int
    id_salida : int
    id_insumo : int
    cantidad : int
    motivo : str
    observacion : str