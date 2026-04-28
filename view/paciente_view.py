import reflex as rx
from typing import List
from ..models.paciente import paciente
from ..controllers.controlador_paciente import controlador_paciente

# Instanciamos el controlador de paciente
controlador_paciente = controlador_paciente()

class State(rx.State):
    id_editando: int = -1
    nombre: str = ""
    tipo: str = ""
    estado: str = ""
    pacientes: List[paciente] = []

    def cargar_pacientes(self):
        self.pacientes = controlador_paciente.obtener_pacientes()

    def guardar(self):
        controlador_paciente.agregar_paciente(self.nombre, self.tipo, self.estado)
        self.limpiar()
        self.cargar_pacientes()

    def eliminar(self, id):
        controlador_paciente.eliminar_paciente(id)
        self.cargar_pacientes()

    def editar(self, paciente: dict): # Le decimos que espere un diccionario
        self.id_editando = int(paciente["id_paciente"])
        self.nombre = paciente["nombre_paciente"]
        self.tipo = paciente["tipo_acceso"]
        self.estado = paciente["estado"]   

    def actualizar(self):
        controlador_paciente.actualizar_paciente(
            self.id_editando,
            self.nombre,
            self.tipo,
            self.estado
        )
        self.id_editando = -1
        self.limpiar()
        self.cargar_pacientes()

    def limpiar(self):
        self.nombre = ""
        self.tipo = ""
        self.estado = ""


def fila_paciente(p):
    return rx.hstack(
        rx.text(p.nombre_paciente, width="30%"),
        rx.text(p.tipo_acceso, width="30%"),
        rx.text(p.estado, width="30%"),

        rx.button("Editar", on_click=lambda: State.editar(p)),
        rx.button("Eliminar", color="red", on_click=lambda: State.eliminar(p.id_paciente))
    )


def vista_paciente():
    return rx.vstack(
        rx.heading("Sistema de pacientes"),

        rx.input(
            placeholder="Nombre",
            value=State.nombre,
            on_change=State.set_nombre
        ),
        rx.input(
            placeholder="Tipo",
            value=State.tipo,
            on_change=State.set_tipo
        ),
        rx.input(
            placeholder="Estado",
            value=State.estado,
            on_change=State.set_estado
        ),

        rx.cond(
            State.id_editando == -1,
            rx.button("Guardar", on_click=State.guardar),
            rx.button("Actualizar", color="orange", on_click=State.actualizar)
        ),

        rx.button("Cargar pacientes", on_click=State.cargar_pacientes),
        
        rx.cond(
            State.pacientes.length() > 0,
            rx.vstack(
                rx.foreach(State.pacientes, fila_paciente)
            ),
            rx.text("No hay pacientes cargados o la lista es nula")
        ),

        rx.text(State.id_editando)

        
    )