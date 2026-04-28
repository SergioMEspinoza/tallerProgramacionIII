from ..database.base_datos import Database
from ..models.personal import personal

class controlador_personal:
    def __init__(self):
        self.db = Database().get_connection()

    def obtener_personales(self):
        cur = self.db.cursor()
        cur.execute("SELECT id_personal, nombre, sexo, edad, id_usuario FROM personal ORDER BY id_personal")
        
        # Instanciamos el modelo de Reflex
        personales = [personal(
            id_personal=row[0],
            nombre=row[1],
            sexo=row[2],
            edad=row[3],
            id_usuario=row[4]
        ) for row in cur.fetchall()]
        
        cur.close()
        return personales


    def agregar_personal(self,nombre, sexo, edad, id_usuario):
        
        cur = self.db.cursor()

        cur.execute(
            "INSERT INTO personal (nombre, sexo, edad, id_usuario) VALUES (%s, %s, %s, %s)",
            (nombre, sexo, edad, id_usuario)
        )

        self.db.commit()
        cur.close()


    def actualizar_personal(self,id_personal, nombre, sexo, edad):
        
        cur = self.db.cursor()

        cur.execute(
            """UPDATE personal 
            SET nombre=%s, sexo=%s, edad=%s 
            WHERE id_personal=%s""",
            (nombre, sexo, edad, id_personal)
        )

        self.db.commit()
        cur.close()