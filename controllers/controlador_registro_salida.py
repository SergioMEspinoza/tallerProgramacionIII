from ..database.base_datos import Database
from ..models.registro_salida import registro_salida

class controlador_salida:
    def __init__(self):
        self.db = Database().get_connection()

    def obtener_registro_salidas(self):
        cur = self.db.cursor()
        cur.execute("SELECT id_salida, fecha_salida, id_usuario, id_paciente FROM salida ORDER BY id_salida")
        
        # Instanciamos el modelo de Reflex
        salidas = [registro_salida(
            id_salida=row[0],
            fecha_salida=row[1],
            id_usuario=row[2],
            id_paciente=row[3]
        ) for row in cur.fetchall()]
        
        cur.close()
        return salidas


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

    def obtener_stock(self,id_insumo):
        cur = self.db.cursor()
        
        cur.execute(
            """SELECT cantidad_stock 
            FROM insumo 
            WHERE id_insumo=%s
            LIMIT 1""",
            (id_insumo,)
        )
        
        cantidad = cur.fetchone()
        
        cur.close()
        return int(cantidad[0])

    def registrar_salida(self,id_usuario, id_paciente, detalles):
        
        cur = self.db.cursor()

        try:
            # 1. Crear salida
            cur.execute("""
                INSERT INTO salida (id_usuario, id_paciente)
                VALUES (%s, %s)
                RETURNING id_salida
            """, (id_usuario, id_paciente))

            id_salida = cur.fetchone()[0]

            # 2. Procesar detalle
            for item in detalles:

                # Validar stock
                cur.execute(
                    "SELECT cantidad_stock FROM insumo WHERE id_insumo = %s",
                    (item["id_insumo"],)
                )
                stock = cur.fetchone()[0]

                if item["cantidad"] > stock:
                    raise Exception("Stock insuficiente")

                # Insertar detalle
                cur.execute("""
                    INSERT INTO detalle_salida
                    (id_salida, id_insumo, cantidad, motivo, observacion)
                    VALUES (%s, %s, %s, %s, %s)
                """, (
                    id_salida,
                    item["id_insumo"],
                    item["cantidad"],
                    item["motivo"],
                    item["observacion"]
                ))

                # Actualizar stock
                cur.execute("""
                    UPDATE insumo
                    SET cantidad_stock = cantidad_stock - %s
                    WHERE id_insumo = %s
                """, (
                    item["cantidad"],
                    item["id_insumo"]
                ))

            self.db.commit()
            cur.close()
            return "Salida registrada correctamente"

        except Exception as e:
            self.db.rollback()
            return f"Error: {str(e)}"

       