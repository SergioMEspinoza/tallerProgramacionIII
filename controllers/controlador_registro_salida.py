from ..database.base_datos import Database
from ..models.registro_salida import registro_salida

class controlador_paciente:
    def __init__(self):
        self.db = Database().get_connection()

    def obtener_registro_salidas(self):
        cur = self.db.cursor()
        cur.execute("SELECT id_salida, fecha_salida, id_usuario, id_paciente FROM salida ORDER BY id_salida")
        
        # Instanciamos el modelo de Reflex
        pacientes = [registro_salida(
            id_salida=row[0],
            fecha_salida=row[1],
            id_usuario=row[2],
            id_paciente=row[3]
        ) for row in cur.fetchall()]
        
        cur.close()
        return pacientes


    def agregar_registro_salida(self,fecha_salida, id_usuario, id_paciente):
        cur = self.db.cursor()

        cur.execute(
            "INSERT INTO salida (fecha_salida, id_usuario, id_paciente) VALUES (%s, %s, %s)",
            (fecha_salida, id_usuario, id_paciente)
        )

        self.db.commit()
        cur.close()


    def actualizar_registro_salida(self,id_salida,fecha_salida, id_usuario, id_paciente):
        cur = self.db.cursor()

        cur.execute(
            """UPDATE salida 
            SET fecha_salida=%s, id_usuario=%s, id_paciente=%s
            WHERE id_salida=%s""",
            (fecha_salida, id_usuario, id_paciente, id_salida)
        )

        self.db.commit()
        cur.close()