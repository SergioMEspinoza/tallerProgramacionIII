import reflex as rx
from typing import List
from ..models.insumo import insumo
from ..controllers.controlador_categoria import controlador_categoria
from ..controllers.controlador_insumo import controlador_insumo

# Instanciamos el controladores
controlador_insumo = controlador_insumo()
controlador_categoria = controlador_categoria()

class State(rx.State):

    # datos importates para la edicion de un fila de la tabla insumos
    id_editando: int = -1
    nombre_insumo : str = ""
    descripcion_insumo : str = ""
    minimo_stock : int = -1
    cantidad_stock : int = -1
    estado : str = ""
    id_categoria : int = -1

    # lista para los insumos
    insumos : List[insumo] = []

    # listado de categorias para la funcion rx.select
    categorias : List[str] = controlador_categoria.obtener_nombres_categorias()

    #usado en la funcion de seleccionar la categoria 
    nombre_categoria : str = ""

    #atributos auxiliares para los input
    str_minimo_stock : str = ""
    str_cantidad_stock : str = ""

    def cargar_insumos(self):
        self.insumos = controlador_insumo.obtener_insumos()
    
    def cargar_categorias(self):
        self.categorias = controlador_categoria.obtener_nombres_categorias()

    def guardar(self):
        self.id_categoria = controlador_categoria.obtener_id_categoria(self.nombre_categoria)
        self.minimo_stock = int (self.str_minimo_stock)
        self.cantidad_stock = int (self.str_cantidad_stock)
        controlador_insumo.agregar_insumo(self.nombre_insumo, self.descripcion_insumo,self.minimo_stock,self.cantidad_stock,self.id_categoria)
        self.limpiar()
        self.cargar_insumos()

    def eliminar(self, id):
        controlador_insumo.eliminar_insumo(id)
        self.cargar_insumos()
    
    def reestablecer(self, id):
        controlador_insumo.reestablecer_insumo(id)
        self.cargar_insumos()

    def editar(self, insumo: dict): # Le decimos que espere un diccionario
        self.id_editando = int(insumo["id_insumo"])
        self.nombre_insumo = insumo["nombre_insumo"]
        self.descripcion_insumo = insumo["descripcion_insumo"]
        self.minimo_stock = int(insumo["minimo_stock"])
        self.cantidad_stock = int(insumo["cantidad_stock"])
        self.estado = insumo["estado"]
        self.id_categoria = int(insumo["id_categoria"])
        #para editar en los cuadros especificos
        self.nombre_categoria = controlador_categoria.obtener_un_nombre_categoria(insumo["id_categoria"])
        self.str_cantidad_stock = str(insumo["cantidad_stock"])
        self.str_minimo_stock =  str(insumo["minimo_stock"])

    def actualizar(self):
        self.id_categoria = controlador_categoria.obtener_id_categoria(self.nombre_categoria)
        self.minimo_stock = int (self.str_minimo_stock)
        self.cantidad_stock = int (self.str_cantidad_stock)
        controlador_insumo.actualizar_insumo(
            self.id_editando,
            self.nombre_insumo,
            self.descripcion_insumo,
            self.minimo_stock,
            self.cantidad_stock,
            self.id_categoria
        )
        self.id_editando = -1
        self.limpiar()
        self.cargar_insumos()

    def limpiar(self):
        self.nombre_insumo = ""
        self.descripcion_insumo = ""
        self.minimo_stock = -1
        self.cantidad_stock = -1
        self.estado = ""
        self.id_categoria = -1
        self.nombre_categoria = ""
        self.str_minimo_stock = ""
        self.str_cantidad_stock = ""
        


def fila_insumo(p):
    return rx.hstack(
        rx.text(p.nombre_insumo, width="30%"),
        rx.text(p.descripcion_insumo, width="30%"),
        rx.text(p.minimo_stock, width="30%"),
        rx.text(p.cantidad_stock, width="30%"),
        rx.text(p.estado, width="30%"),
        rx.text(p.id_categoria, width="30%"),

        rx.button("Editar", on_click=lambda: State.editar(p)),
        rx.cond(
            p.estado == "activo",
            rx.button("Eliminar", color="red", on_click=lambda: State.eliminar(p.id_insumo)),
            rx.button("Reestablecer", color="blue", on_click=lambda: State.reestablecer(p.id_insumo))
        )
    )


def vista_insumo():
    return rx.vstack(
        rx.heading("Sistema de insumos"),

        rx.input(
            placeholder="Nombre del insumo",
            value=State.nombre_insumo,
            on_change=State.set_nombre_insumo
        ),
        rx.input(
            placeholder="descripcion",
            value=State.descripcion_insumo,
            on_change=State.set_descripcion_insumo
        ),
        rx.input(
            placeholder="minimo stock",
            value=State.str_minimo_stock,
            on_change=State.set_str_minimo_stock
        ),

        rx.input(
            placeholder="cantidad stock",
            value=State.str_cantidad_stock,
            on_change=State.set_str_cantidad_stock
        ),

        rx.select(
            State.categorias,
            value=State.nombre_categoria,
            on_change=State.set_nombre_categoria,
            placeholder="Seleccione la categoria"
        ),

        rx.cond(
            State.id_editando == -1,
            rx.button("Guardar", on_click=State.guardar),
            rx.button("Actualizar", color="orange", on_click=State.actualizar)
        ),

        rx.button("Cargar insumos", on_click=State.cargar_insumos),
        
        rx.cond(
            State.insumos.length() > 0,
            rx.vstack(
                rx.foreach(State.insumos, fila_insumo)
            ),
            rx.text("No hay insumos cargados o la lista es nula")
        ),

        rx.text(State.id_editando)

        
    )