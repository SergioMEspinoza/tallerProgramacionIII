from ..database.base_datos import Database
from ..models.detalle_entrada import detalle_entrada

class controlador_paciente:
    def __init__(self):
        self.db = Database().get_connection()

    def obtener_detalle_entradas(self):
        cur = self.db.cursor()
        cur.execute("SELECT id_detalle_entrada, id_entrada, id_insumo, cantidad FROM detalle_entrada ORDER BY id_detalle_entrada")
        
        # Instanciamos el modelo de Reflex
        pacientes = [detalle_entrada(
            id_detalle_entrada=row[0], 
            id_entrada=row[1], 
            id_insumo=row[2], 
            cantidad=row[3] 
        ) for row in cur.fetchall()]
        
        cur.close()
        return pacientes


    def agregar_detalle_entrada(self,id_entrada, id_insumo, cantidad):
        cur = self.db.cursor()

        cur.execute(
            "INSERT INTO detalle_entrada (id_entrada, id_insumo, cantidad) VALUES (%s, %s, %s)",
            (id_entrada, id_insumo, cantidad)
        )

        self.db.commit()
        cur.close()


    def actualizar_detalle_entrada(self,id_detalle_entrada,id_entrada, id_insumo, cantidad):
        cur = self.db.cursor()

        cur.execute(
            """UPDATE detalle_entrada 
            SET id_entrada=%s, id_insumo=%s, cantidad=%s 
            WHERE id_detalle_entrada=%s""",
            (id_entrada, id_insumo, cantidad, id_detalle_entrada)
        )

        self.db.commit()
        cur.close()