from ..database.base_datos import Database
from ..models.detalle_salida import detalle_salida

class controlador_paciente:
    def __init__(self):
        self.db = Database().get_connection()

    def obtener_detalle_salidas(self):
        cur = self.db.cursor()
        cur.execute("SELECT id_detalle_salida, id_salida, id_insumo, cantidad, motivo, observacion FROM detalle_salida ORDER BY id_detalle_salida")
        
        # Instanciamos el modelo de Reflex
        pacientes = [detalle_salida(
            id_detalle_salida=row[0],
            id_salida=row[1],
            id_insumo=row[2],
            cantidad=row[3],
            motivo=row[4],
            observacion=row[5]
        ) for row in cur.fetchall()]
        
        cur.close()
        return pacientes


    def agregar_detalle_salida(self,id_salida, id_insumo, cantidad, motivo, observacion):
        cur = self.db.cursor()

        cur.execute(
            "INSERT INTO detalle_salida (id_salida, id_insumo, cantidad, motivo, observacion) VALUES (%s, %s, %s, %s, %s)",
            (id_salida, id_insumo, cantidad, motivo, observacion)
        )

        self.db.commit()
        cur.close()


    def actualizar_detalle_salida(self,id_detalle_salida,id_salida, id_insumo, cantidad, motivo, observacion):
        cur = self.db.cursor()

        cur.execute(
            """UPDATE detalle_salida 
            SET id_salida=%s, id_insumo=%s, cantidad=%s, motivo=%s, observacion=%s 
            WHERE id_detalle_salida=%s""",
            (id_salida, id_insumo, cantidad, motivo, observacion, id_detalle_salida)
        )

        self.db.commit()
        cur.close()