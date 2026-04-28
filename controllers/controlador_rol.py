from ..database.base_datos import Database
from ..models.rol import rol

class controlador_rol:
    def __init__(self):
        self.db = Database().get_connection()

    def obtener_roles(self):
        
        cur = self.db.cursor()
        cur.execute("SELECT id_rol, nombre_rol FROM rol ORDER BY id_rol")
        
        # Instanciamos el modelo de Reflex
        roles = [rol(
            id_rol=row[0],
            nombre_rol=row[1]
        ) for row in cur.fetchall()]
        
        cur.close()
        return roles


    def agregar_rol(self,nombre_rol):
        
        cur = self.db.cursor()

        cur.execute(
            "INSERT INTO rol (nombre_rol) VALUES (%s)",
            (nombre_rol)
        )

        self.db.commit()
        cur.close()



    def actualizar_rol(self,id_rol, nombre_rol):
        
        cur = self.db.cursor()

        cur.execute(
            """UPDATE rol 
            SET nombre_rol=%s 
            WHERE id_rol=%s""",
            (nombre_rol, id_rol)
        )

        self.db.commit()
        cur.close()