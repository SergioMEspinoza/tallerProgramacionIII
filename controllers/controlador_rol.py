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

    def obtener_nombres_roles(self):
        cur = self.db.cursor()
        cur.execute("SELECT nombre_rol FROM rol ORDER BY id_rol")
        
        # Instanciamos el modelo de Reflex
        roles = [row[0] for row in cur.fetchall()]
        
        cur.close()
        return roles
    
    def obtener_id_rol(self,nombre_rol):
        cur = self.db.cursor()
        
        cur.execute(
            """SELECT id_rol 
            FROM rol 
            WHERE nombre_rol=%s
            LIMIT 1""",
            (nombre_rol,)
        )
        
        id = cur.fetchone()
        
        cur.close()
        return int(id[0])
    
    def obtener_un_nombre_rol(self,id_rol):
        cur = self.db.cursor()
        
        cur.execute(
            """SELECT nombre_rol 
            FROM rol 
            WHERE id_rol=%s
            LIMIT 1""",
            (id_rol,)
        )
        
        nombre = cur.fetchone()
        
        cur.close()
        return str(nombre[0])

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