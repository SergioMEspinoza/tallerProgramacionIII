from ..database.base_datos import Database
from ..models.insumo import insumo

class controlador_insumo:
    def __init__(self):
        self.db = Database().get_connection()
        
    def obtener_insumos(self):
        
        cur = self.db.cursor()
        cur.execute("SELECT id_insumo, nombre_insumo, descripcion_insumo, minimo_stock, cantidad_stock, estado, id_categoria FROM insumo ORDER BY id_insumo")
        
        # Instanciamos el modelo de Reflex
        insumos = [insumo(
            id_insumo=row[0],
            nombre_insumo=row[1],
            descripcion_insumo=row[2],
            minimo_stock=row[3],
            cantidad_stock=row[4],
            estado=row[5],
            id_categoria=row[6]
        ) for row in cur.fetchall()]
        
        cur.close()
        return insumos


    def agregar_insumo(self,nombre_insumo, descripcion_insumo, minimo_stock, cantidad_stock, id_categoria):
        
        cur = self.db.cursor()

        cur.execute(
            "INSERT INTO insumo (nombre_insumo, descripcion_insumo, minimo_stock, cantidad_stock, id_categoria) VALUES (%s, %s, %s, %s, %s)",
            (nombre_insumo, descripcion_insumo, minimo_stock, cantidad_stock, id_categoria)
        )

        self.db.commit()
        cur.close()


    def eliminar_insumo(self,id_insumo):
        
        cur = self.db.cursor()

        cur.execute(
            """UPDATE insumo 
            SET estado='eliminado'
            WHERE id_insumo=%s""",
            (id_insumo,)
        )
        
        self.db.commit()
        cur.close()

    def reestablecer_insumo(self,id_insumo):
        
        cur = self.db.cursor()

        cur.execute(
            """UPDATE insumo 
            SET estado='activo'
            WHERE id_insumo=%s""",
            (id_insumo,)
        )
        
        self.db.commit()
        cur.close()


    def actualizar_insumo(self,id_insumo, nombre_insumo, descripcion_insumo, minimo_stock, cantidad_stock, id_categoria):
        
        cur = self.db.cursor()

        cur.execute(
            """UPDATE insumo 
            SET nombre_insumo=%s, descripcion_insumo=%s, minimo_stock=%s, cantidad_stock=%s, id_categoria=%s 
            WHERE id_insumo=%s""",
            (nombre_insumo, descripcion_insumo, minimo_stock, cantidad_stock, id_categoria, id_insumo)
        )

        self.db.commit()
        cur.close()