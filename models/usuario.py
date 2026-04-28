from pydantic import BaseModel

class usuario(BaseModel):
    id_usuario : int
    nombre_usuario : str
    email : str
    contrasena : str
    estado : str
    id_rol : int