from ..database.base_datos import Database
from ..models.usuario import usuario

class controlador_usuario:
    def __init__(self):
        self.db = Database().get_connection()

    def obtener_usuarios(self):
        
        cur = self.db.cursor()
        cur.execute("SELECT id_usuario, nombre_usuario, email, contrasena, estado, id_rol FROM usuario ORDER BY id_usuario")
        
        # Instanciamos el modelo de Reflex
        usuarios = [usuario(
            id_usuario=row[0],
            nombre_usuario=row[1],
            email=row[2],
            contrasena=row[3],
            estado=row[4],
            id_rol=row[5]
        ) for row in cur.fetchall()]
        
        cur.close()
        return usuarios


    def agregar_usuario(self,usuario):
        
        cur = self.db.cursor()

        cur.execute(
            "INSERT INTO usuario (nombre_usuario, email, contrasena, id_rol) VALUES (%s, %s, %s, %s)",
            (usuario.nombre_usuario, usuario.email, usuario.contrasena, usuario.id_rol)
        )

        self.db.commit()
        cur.close()


    def eliminar_usuario(self,id_usuario):
        
        cur = self.db.cursor()

        cur.execute(
            """UPDATE usuario 
            SET estado='Eliminado'
            WHERE id_usuario=%s""",
            (id_usuario,)
        )
        
        self.db.commit()
        cur.close()
    
    def reestablecer_usuario(self,id_usuario):
        
        cur = self.db.cursor()

        cur.execute(
            """UPDATE usuario 
            SET estado='Activo'
            WHERE id_usuario=%s""",
            (id_usuario,)
        )
        
        self.db.commit()
        cur.close()
    
    #esta funcion servira para el registro de los datos personales del usuario
    def devolver_el_ultimo_id(self):
        
        cur = self.db.cursor()
        
        cur.execute(
            """SELECT MAX(id_usuario) AS valor_maximo 
            FROM usuario"""
        )
        
        id = cur.fetchone()
        
        cur.close()
        return int(id[0])


    def actualizar_usuario(self,usuario):
        
        cur = self.db.cursor()

        cur.execute(
            """UPDATE usuario 
            SET nombre_usuario=%s, email=%s, contrasena=%s, id_rol=%s 
            WHERE id_usuario=%s""",
            (usuario.nombre_usuario, usuario.email, usuario.contrasena, usuario.id_rol, usuario.id_usuario)
        )

        self.db.commit()
        cur.close()