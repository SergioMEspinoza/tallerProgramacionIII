import reflex as rx
from .state import InventoryState, InsumoSchema

def tarjeta_estadistica(titulo: str, valor: str, icono: str, color: str):
    """Crea una tarjeta visual de indicadores."""
    return rx.box(
        rx.vstack(
            rx.text(icono, font_size="2em"),
            rx.text(valor, font_size="1.8em", font_weight="bold", color=color),
            rx.text(titulo, font_size="0.9em", color="gray"),
            align="center",
            spacing="1",
        ),
        border=f"1px solid {color}",
        padding="1em",
        border_radius="lg",
        background="white",
        width="100%",
    )

def render_fila_tabla(insumo: InsumoSchema):
    """Renderiza cada fila de la tabla de insumos."""
    return rx.table.row(
        rx.table.cell(insumo.id),
        rx.table.cell(insumo.nombre),
        rx.table.cell(insumo.cantidad),
        rx.table.cell(insumo.vencimiento),
    )

def vista_login() -> rx.Component:
    """Pantalla de acceso inicial."""
    return rx.center(
        rx.card(
            rx.vstack(
                rx.heading("Clínica de Hemodiálisis SALUVIT S.A.", as_="h1", size="9", color_scheme="blue"),
                rx.heading("SySControl v. 1.1.0", as_="h2", size="7", color_scheme="blue"),
                rx.input(placeholder="Usuario", 
                         on_change=InventoryState.set_usuario_logueado, 
                         bg="gray"),
                rx.input(placeholder="Contraseña", type="password", 
                         on_change=InventoryState.set_password_input, 
                         bg="gray"),
                rx.center(
                    rx.button("Entrar", on_click=InventoryState.login, width="100px", color_scheme="teal"),
                    width="100%",
                ),
                spacing="4",
            ),
            padding="2em",
        ),
        height="100vh",
        background="#f4f6f8"
    )

def navbar() -> rx.Component:
    return rx.hstack(
        rx.heading("Sistema Hemodiálisis", size="6"),
        rx.spacer(),
        rx.badge(InventoryState.rol_usuario, color_scheme="green", variant="surface"),
        rx.button("Cerrar Sesión", on_click=InventoryState.logout, size="2", color_scheme="red", variant="ghost"),
        width="100%",
        padding="1em",
        border_bottom="1px solid #eaeaea",
    )
    
def formulario_registro() -> rx.Component:
    """Formulario de registro, protegido por Rol."""
    # rx.cond verifica si es Admin. Si lo es, dibuja el card. Si no, no dibuja nada.
    return rx.cond(
        InventoryState.rol_usuario == "admin",
        rx.card(
            rx.vstack(
                rx.heading("Registro de Nuevo Insumo", size="4"),
                rx.input(
                    placeholder="Nombre del Insumo", 
                    on_change=InventoryState.set_nuevo_nombre, # Conexión al setter explícito
                    value=InventoryState.nuevo_nombre
                ),
                rx.hstack(
                    rx.input(
                        placeholder="Cantidad", 
                        type="number", 
                        on_change=InventoryState.set_nueva_cantidad, # Conexión al setter explícito
                        value=InventoryState.nueva_cantidad
                    ),
                    rx.input(
                        type="date", 
                        on_change=InventoryState.set_nueva_fecha, # Conexión al setter explícito
                        value=InventoryState.nueva_fecha
                    ),
                    width="100%",
                ),
                rx.button(
                    "Guardar en Base de Datos", 
                    on_click=InventoryState.agregar_insumo_local, 
                    width="100%", 
                    color_scheme="blue"
                ),
                spacing="3",
            ),
            padding="2em",
            margin_bottom="2em",
            width="100%",
        )
    )