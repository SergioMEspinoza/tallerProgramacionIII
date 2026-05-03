from ..database.base_datos import Database
from ..models.registro_entrada import registro_entrada

class controlador_entrada:
    def __init__(self):
        self.db = Database().get_connection()

    def obtener_registro_entradas(self):
        cur = self.db.cursor()
        cur.execute("SELECT id_entrada, fecha_entrada, id_usuario FROM entrada ORDER BY id_entrada")
        
        # Instanciamos el modelo de Reflex
        entradas = [registro_entrada(
            id_entrada=row[0],
            fecha_entrada=row[1],
            id_usuario=row[2]
        ) for row in cur.fetchall()]
        
        cur.close()
        return entradas


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

    def registrar_entrada(self,id_usuario, detalles):

        
        cur = self.db.cursor()

        try:
            # 1. Insertar entrada principal
            cur.execute("""
                INSERT INTO entrada (id_usuario)
                VALUES (%s)
                RETURNING id_entrada
            """, (id_usuario,))

            id_entrada = cur.fetchone()[0]

            # 2. Insertar detalles
            for item in detalles:
                cur.execute("""
                    INSERT INTO detalle_entrada
                    (id_entrada, id_insumo, cantidad)
                    VALUES (%s, %s, %s)
                """, (
                    id_entrada,
                    item["id_insumo"],
                    item["cantidad"]
                ))

                # 3. Actualizar stock
                cur.execute("""
                    UPDATE insumo
                    SET cantidad_stock = cantidad_stock + %s
                    WHERE id_insumo = %s
                """, (
                    item["cantidad"],
                    item["id_insumo"]
                ))

            self.db.commit()
            cur.close()
            return "Entrada registrada correctamente"

        except Exception as e:
            self.db.rollback()
            return f"Error: {str(e)}"
