from ..database.base_datos import Database
from ..models.registro_entrada import registro_entrada

class controlador_paciente:
    def __init__(self):
        self.db = Database().get_connection()

    def obtener_registro_entradas(self):
        cur = self.db.cursor()
        cur.execute("SELECT id_entrada, fecha_entrada, id_usuario FROM entrada ORDER BY id_entrada")
        
        # Instanciamos el modelo de Reflex
        pacientes = [registro_entrada(
            id_entrada=row[0],
            fecha_entrada=row[1],
            id_usuario=row[2]
        ) for row in cur.fetchall()]
        
        cur.close()
        return pacientes


    def agregar_registro_entrada(self,fecha_entrada, id_usuario):
        cur = self.db.cursor()

        cur.execute(
            "INSERT INTO entrada (fecha_entrada, id_usuario) VALUES (%s, %s)",
            (fecha_entrada, id_usuario)
        )

        self.db.commit()
        cur.close()


    def actualizar_registro_entrada(self,id_entrada, fecha_entrada, id_usuario):
        cur = self.db.cursor()

        cur.execute(
            """UPDATE entrada 
            SET fecha_entrada=%s, id_usuario=%s 
            WHERE id_entrada=%s""",
            (id_entrada, fecha_entrada, id_usuario, id_entrada)
        )

        self.db.commit()
        cur.close()