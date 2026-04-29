from pydantic import BaseModel

class usuario(BaseModel):
    id_usuario : int = -1
    nombre_usuario : str = ""
    email : str = ""
    contrasena : str = ""
    estado : str = ""
    id_rol : int = -1

    
    def borrar(self):
        self.id_usuario = -1
        self.nombre_usuario = ""
        self.email = ""
        self.contrasena = ""
        self.estado = ""
        self.id_rol = -1