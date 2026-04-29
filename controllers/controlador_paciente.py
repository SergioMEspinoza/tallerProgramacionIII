from ..database.base_datos import Database
from ..models.paciente import paciente

class controlador_paciente:
    def __init__(self):
        self.db = Database().get_connection()

    def obtener_pacientes(self):
        cur = self.db.cursor()
        cur.execute("SELECT id_paciente, nombre_paciente, tipo_acceso, estado FROM paciente ORDER BY id_paciente")
        
        # Instanciamos el modelo de Reflex
        pacientes = [paciente(
            id_paciente=row[0], 
            nombre_paciente=row[1], 
            tipo_acceso=row[2], 
            estado=row[3]
        ) for row in cur.fetchall()]
        
        cur.close()
        return pacientes


    def agregar_paciente(self,nombre, tipo_acceso):
        cur = self.db.cursor()

        cur.execute(
            "INSERT INTO paciente (nombre_paciente, tipo_acceso) VALUES (%s, %s)",
            (nombre, tipo_acceso)
        )

        self.db.commit()
        cur.close()


    def eliminar_paciente(self,id_paciente):
        cur = self.db.cursor()

        cur.execute(
            """UPDATE paciente 
            SET estado='Eliminado'
            WHERE id_paciente=%s""",
            (id_paciente,)
        )
        
        self.db.commit()
        cur.close()

    def reestablecer_paciente(self,id_paciente):
        cur = self.db.cursor()

        cur.execute(
            """UPDATE paciente 
            SET estado='Activo'
            WHERE id_paciente=%s""",
            (id_paciente,)
        )
        
        self.db.commit()
        cur.close()

    def reestablecer_paciente(self,id_paciente):
        
        cur = self.db.cursor()

        cur.execute(
            """UPDATE paciente 
            SET estado='Activo'
            WHERE id_paciente=%s""",
            (id_paciente,)
        )
        
        self.db.commit()
        cur.close()


    def actualizar_paciente(self,id_paciente, nombre, tipo_acceso):
        cur = self.db.cursor()

        cur.execute(
            """UPDATE paciente 
            SET nombre_paciente=%s, tipo_acceso=%s
            WHERE id_paciente=%s""",
            (nombre, tipo_acceso, id_paciente)
        )

        self.db.commit()
        cur.close()