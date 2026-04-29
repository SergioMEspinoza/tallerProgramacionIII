from pydantic import BaseModel

class personal(BaseModel):
    id_personal : int = -1
    nombre : str = ""
    sexo : str = ""
    edad : int = -1
    id_usuario : int = -1
    
    def borrar(self):
        self.nombre = ""
        self.edad = -1
        self.id_personal = -1
        self.sexo = ""
        self.id_usuario = -1