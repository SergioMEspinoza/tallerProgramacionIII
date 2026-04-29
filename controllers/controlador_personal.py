from ..database.base_datos import Database
from ..models.personal import personal
from psycopg2.extras import RealDictCursor

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
    
    def obtener_datos_personales_de_un_usario(self,id_usuario):

        cur = self.db.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT id_personal, nombre, sexo, edad, id_usuario FROM personal WHERE id_usuario = %s LIMIT 1", (id_usuario,))
        datos = cur.fetchone()
        
        cur.close()
        return datos


    def agregar_personal(self,personal):
        
        cur = self.db.cursor()

        cur.execute(
            "INSERT INTO personal (nombre, sexo, edad, id_usuario) VALUES (%s, %s, %s, %s)",
            (personal.nombre, personal.sexo, personal.edad, personal.id_usuario)
        )

        self.db.commit()
        cur.close()


    def actualizar_personal(self,personal):
        
        cur = self.db.cursor()

        cur.execute(
            """UPDATE personal 
            SET nombre=%s, sexo=%s, edad=%s 
            WHERE id_personal=%s""",
            (personal.nombre, personal.sexo, personal.edad, personal.id_personal)
        )

        self.db.commit()
        cur.close()