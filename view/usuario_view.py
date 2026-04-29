import reflex as rx
from typing import List
from ..models.usuario import usuario
from ..models.personal import personal
from ..controllers.controlador_rol import controlador_rol
from ..controllers.controlador_usuario import controlador_usuario
from ..controllers.controlador_personal import controlador_personal

# Instanciamos el controlador de paciente
controlador_usuario = controlador_usuario()
controlador_personal = controlador_personal()
controlador_rol = controlador_rol()

class State(rx.State):

    # datos importates para la edicion de un fila de la tabla 
    usuario_editar = usuario()
    usuario_editar.borrar()
    personal_editar = personal()
    personal_editar.borrar()
    

    # lista para los usuarios
    usuarios : List[usuario] = []

    # listado de categorias para la funcion rx.select
    roles : List[str] = controlador_rol.obtener_nombres_roles()

    #usado en la funcion de seleccionar el rol
    nombre_rol : str = ""

    #atributos auxiliares para los input del personal
    str_edad : str = ""

    #set para cambio de informacion con los inputs
    @rx.event
    def set_nombre_usuario(self, value: str):
        self.usuario_editar.nombre_usuario = value
    
    @rx.event
    def set_email(self, value: str):
        self.usuario_editar.email = value
    
    @rx.event
    def set_contrasena(self, value: str):
        self.usuario_editar.contrasena = value

    @rx.event
    def set_nombre(self, value: str):
        self.personal_editar.nombre = value

    @rx.event
    def set_sexo(self, value: str):
        self.personal_editar.sexo = value

    def cargar_usuarios(self):
        self.usuarios = controlador_usuario.obtener_usuarios()
    
    def cargar_roles(self):
        self.categorias = controlador_rol.obtener_nombres_roles()

    def guardar(self):
        self.usuario_editar.id_rol = controlador_rol.obtener_id_rol(self.nombre_rol)
        self.personal_editar.edad = int (self.str_edad)
        controlador_usuario.agregar_usuario(self.usuario_editar)
        self.personal_editar.id_usuario = controlador_usuario.devolver_el_ultimo_id()
        controlador_personal.agregar_personal(self.personal_editar)
        self.limpiar()
        self.cargar_usuarios()

    def eliminar(self, id):
        controlador_usuario.eliminar_usuario(id)
        self.cargar_usuarios()
    
    def reestablecer(self, id):
        controlador_usuario.reestablecer_usuario(id)
        self.cargar_usuarios()

    def editar(self, usuario: dict): # Le decimos que espere un diccionario

        #editar los atributos del usuario
        self.usuario_editar.id_usuario = int(usuario["id_usuario"])
        self.usuario_editar.nombre_usuario = usuario["nombre_usuario"]
        self.usuario_editar.email = usuario["email"]
        self.usuario_editar.contrasena = usuario["contrasena"]
        self.usuario_editar.estado = usuario["estado"]
        self.usuario_editar.id_rol = int(usuario["id_rol"])

        #para obtener la informacion personal del usario a editar
        datos : dict = controlador_personal.obtener_datos_personales_de_un_usario(usuario["id_usuario"])

        #editar los atributos de los datos personales del usuario
        self.personal_editar.id_personal = int(datos["id_personal"])
        self.personal_editar.nombre = datos["nombre"]
        self.personal_editar.sexo = datos["sexo"]
        self.personal_editar.edad = int(datos["edad"])
        self.personal_editar.id_usuario = int(datos["id_usuario"])

        #para editar en los cuadros especificos
        self.nombre_rol = controlador_rol.obtener_un_nombre_rol(usuario["id_rol"])
        self.str_edad = str(datos["edad"])

    def actualizar(self):
        self.usuario_editar.id_rol = controlador_rol.obtener_id_rol(self.nombre_rol)
        self.personal_editar.edad = int (self.str_edad)
        controlador_usuario.actualizar_usuario(self.usuario_editar)
        controlador_personal.actualizar_personal(self.personal_editar)
        self.limpiar()
        self.cargar_usuarios()

    def limpiar(self):
        self.usuario_editar.borrar()
        self.personal_editar.borrar()
        self.nombre_rol = ""
        self.str_edad = ""
        


def fila_usuario(p):
    return rx.hstack(
        rx.text(p.id_usuario, width="30%"),
        rx.text(p.nombre_usuario, width="30%"),
        rx.text(p.email, width="30%"),
        rx.text(p.contrasena, width="30%"),
        rx.text(p.estado, width="30%"),
        rx.text(p.id_rol, width="30%"),

        rx.button("Editar", on_click=lambda: State.editar(p)),
        rx.cond(
            p.estado == "Activo",
            rx.button("Eliminar", color="red", on_click=lambda: State.eliminar(p.id_usuario)),
            rx.button("Reestablecer", color="blue", on_click=lambda: State.reestablecer(p.id_usuario))
        )
    )


def vista_usuario():
    return rx.vstack(
        rx.heading("Sistema de usuarios"),

        rx.input(
            placeholder="nombre de usuario",
            value=State.usuario_editar.nombre_usuario,
            on_change=State.set_nombre_usuario
        ),
        rx.input(
            placeholder="email",
            value=State.usuario_editar.email,
            on_change=State.set_email
        ),
        rx.input(
            placeholder="contrasena",
            value=State.usuario_editar.contrasena,
            on_change=State.set_contrasena
        ),

        rx.select(
            State.roles,
            value=State.nombre_rol,
            on_change=State.set_nombre_rol,
            placeholder="Seleccione el rol"
        ),

        rx.divider(),

        rx.heading("Datos personales"),

        rx.input(
            placeholder="nombre",
            value=State.personal_editar.nombre,
            on_change=State.set_nombre
        ),

        rx.input(
            placeholder="edad",
            value=State.str_edad,
            on_change=State.set_str_edad
        ),

        rx.select(
            ["Masculino","Femenino"],
            value=State.personal_editar.sexo,
            on_change=State.set_sexo,
            placeholder="Seleccione el sexo"
        ),

        rx.cond(
            State.usuario_editar.id_usuario == -1,
            rx.button("Guardar", on_click=State.guardar),
            rx.button("Actualizar", color="orange", on_click=State.actualizar)
        ),

        rx.button("Cargar usuarios", on_click=State.cargar_usuarios),
        
        rx.cond(
            State.usuarios.length() > 0,
            rx.vstack(
                rx.foreach(State.usuarios, fila_usuario)
            ),
            rx.text("No hay usuarios cargados o la lista es nula")
        ),

        rx.text(State.usuario_editar.id_usuario)

        
    )