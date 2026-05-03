import reflex as rx
from typing import List, Dict, Any
from ..models.insumo import insumo
from ..controllers.controlador_registro_salida import controlador_salida
from ..controllers.controlador_insumo import controlador_insumo

# Instanciamos el controladores
controlador_insumo = controlador_insumo()
controlador_salida = controlador_salida()

class SalidaState(rx.State):
    # Datos temporales del formulario
    id_temporal: int = 0
    cantidad: int = 0
    motivo: str = ""
    observacion: str = ""

    # Lista temporal de insumos agregados
    detalles: List[Dict[str, Any]] = []

    # Insumoa cargados desde BD
    insumos : List[insumo] = []
    mensaje: str = ""

    # Simulación de usuario logueado
    id_usuario: int = 1
    id_paciente: int = 1

    def set_id_temporal(self, valor: str):
        try:
            self.id_temporal = int(valor)
        except:
            self.id_temporal = 0

    def set_cantidad(self, valor: str):
        try:
            self.cantidad = int(valor)
        except:
            self.cantidad = 0

    def cargar_insumos(self):
        self.insumos = controlador_insumo.obtener_insumos()

    def agregar_detalle(self):
        if self.id_temporal == 0:
            self.mensaje = "Seleccione un insumo"
            return

        if self.cantidad <= 0:
            self.mensaje = "La cantidad debe ser mayor a 0"
            return

        # Buscar nombre del producto
        nombre_insumo = ""
        for p in self.insumos:
            if p.id_insumo == self.id_temporal:
                nombre_insumo = p.nombre_insumo
                break
        
        cant_aux = controlador_salida.obtener_stock(self.id_temporal)
        #  VALIDACIÓN CLAVE
        if self.cantidad > cant_aux:
            self.mensaje = f"Stock insuficiente (Disponible: {cant_aux})"
            return

        # Agregar a lista temporal
        self.detalles.append({
            "id_insumo": self.id_temporal,
            "nombre_insumo": nombre_insumo,
            "cantidad": self.cantidad,
            "motivo": self.motivo,
            "observacion": self.observacion
        })

        # Limpiar formulario
        self.id_temporal = 0
        self.cantidad = 0
        self.motivo = ""
        self.observacion = ""
        self.mensaje = "Insumo agregado correctamente"

    def eliminar_detalle(self, index):
        self.detalles.pop(index)
        self.mensaje = "Insumo eliminado de la lista"

    def guardar_salida(self):
        if len(self.detalles) == 0:
            self.mensaje = "Debe agregar al menos un insumo"
            return

        try:
            resultado = controlador_salida.registrar_salida(
                self.id_usuario,
                self.id_paciente,
                self.detalles
            )

            self.mensaje = resultado

            # Limpiar después de guardar
            self.detalles.clear()
            self.detalles = []
            self.id_temporal = 0
            self.cantidad = 0
            self.motivo = ""
            self.observacion = ""

        except Exception as e:
            self.mensaje = f"Error: {str(e)}"


def fila_detalle(item, index):
    return rx.hstack(
        rx.text(item["nombre_insumo"], width="40%"),
        # Eliminamos rx.format y usamos una concatenación simple o f-string de Reflex
        rx.text(f"Cantidad: {item['cantidad']}", width="30%"),
        rx.text(f"Motivo: {item['motivo']}", width="20%"),
        rx.text(item["observacion"], width="25%"),

        rx.button(
            "Eliminar",
            color_scheme="red",
            on_click=lambda: SalidaState.eliminar_detalle(index)
        ),
        width="100%",
    )


def vista_salida():
    return rx.vstack(

        rx.heading("Registro de Salidas de Productos"),

        # Selector de insumos
        rx.select.root(
            # El trigger es lo que el usuario ve (el botón del select)
            rx.select.trigger(placeholder="Seleccione un insumo"),
            
            # El contenido es el menú desplegable
            rx.select.content(
                rx.foreach(
                    SalidaState.insumos,
                    lambda p: rx.select.item(
                        # Usamos f-string para el texto mostrado
                        f"{p.id_insumo} - {p.nombre_insumo}",
                        # El value debe ser string para el componente Select
                        value=p.id_insumo.to_string()
                    )
                )
            ),
            # El evento va en el componente Root
            on_change=lambda v: SalidaState.set_id_temporal(v),
        ),

        # Cantidad
        rx.input(
            placeholder="Cantidad",
            type="number",
            value=SalidaState.cantidad.to_string(),
            on_change=lambda value: SalidaState.set_cantidad(value)
        ),

        # Motivo
        rx.input(
            placeholder="Motivo",
            value=SalidaState.motivo,
            on_change=SalidaState.set_motivo
        ),

        # Observación
        rx.text_area(
            placeholder="Observación",
            value=SalidaState.observacion,
            on_change=SalidaState.set_observacion
        ),

        # Botón agregar
        rx.button(
            "Agregar Insumo",
            on_click=SalidaState.agregar_detalle
        ),

        rx.divider(),

        rx.heading("Detalle de Salida"),

        rx.cond(
            SalidaState.detalles.length() == 0,
            rx.text("No hay productos agregados"),
            rx.vstack(
                rx.foreach(
                    SalidaState.detalles,
                    lambda item, i: fila_detalle(item, i)
                )
            )
        ),

        rx.button(
            "Guardar Salida Completa",
            size="4",
            on_click=SalidaState.guardar_salida
        ),

        rx.text(
            SalidaState.mensaje,
            font_weight="bold"
        ),

        # Cargar insumos al abrir la vista
        on_mount=SalidaState.cargar_insumos,

        spacing="4",
        width="60%",
        padding="30px",
    )
