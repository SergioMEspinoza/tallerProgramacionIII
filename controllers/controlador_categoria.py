from ..database.base_datos import Database
from ..models.categoria import categoria

class controlador_categoria:
    def __init__(self):
        self.db = Database().get_connection()

    def obtener_categorias(self):
        cur = self.db.cursor()
        cur.execute("SELECT id_categoria, nombre_categoria FROM categoria ORDER BY id_categoria")
        
        # Instanciamos el modelo de Reflex
        categorias = [categoria(
            id_categoria=row[0],
            nombre_categoria=row[1]
        ) for row in cur.fetchall()]
        
        cur.close()
        return categorias
    
    def obtener_nombres_categorias(self):
        cur = self.db.cursor()
        cur.execute("SELECT nombre_categoria FROM categoria ORDER BY id_categoria")
        
        # Instanciamos el modelo de Reflex
        categorias = [row[0] for row in cur.fetchall()]
        
        cur.close()
        return categorias
    
    def obtener_id_categoria(self,nombre_categoria):
        cur = self.db.cursor()
        
        cur.execute(
            """SELECT id_categoria 
            FROM categoria 
            WHERE nombre_categoria=%s
            LIMIT 1""",
            (nombre_categoria,)
        )
        # Instanciamos el modelo de Reflex
        id = cur.fetchone()
        
        cur.close()
        return int(id[0])
    
    def obtener_un_nombre_categoria(self,id_categoria):
        cur = self.db.cursor()
        
        cur.execute(
            """SELECT nombre_categoria 
            FROM categoria 
            WHERE id_categoria=%s
            LIMIT 1""",
            (id_categoria,)
        )
        # Instanciamos el modelo de Reflex
        nombre = cur.fetchone()
        
        cur.close()
        return str(nombre[0])


    def agregar_categoria(self,nombre_categoria):
        
        cur = self.db.cursor()

        cur.execute(
            "INSERT INTO categoria (nombre_categoria) VALUES (%s)",
            (nombre_categoria,)
        )

        self.db.commit()
        cur.close()



    def actualizar_categoria(self,id_categoria, nombre_categoria):
        
        cur = self.db.cursor()

        cur.execute(
            """UPDATE categoria 
            SET nombre_categoria=%s 
            WHERE id_categoria=%s""",
            (nombre_categoria, id_categoria)
        )

        self.db.commit()
        cur.close()