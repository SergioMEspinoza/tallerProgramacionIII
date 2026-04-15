import reflex as rx
from .state import InventoryState
from .components import vista_login, navbar, tarjeta_estadistica, render_fila_tabla, formulario_registro

def dashboard_principal() -> rx.Component:
    """Esta es la vista protegida que solo ven usuarios logueados."""
    return rx.container(
        navbar(),
        
        # 1. ESTADÍSTICAS (Visibles para Admin y Médico, según PDF)
        rx.cond(
            (InventoryState.rol_usuario == "admin") | (InventoryState.rol_usuario == "medico"),
            rx.grid(
                tarjeta_estadistica("Stock Actual", "1,240", "📦", "blue"),
                tarjeta_estadistica("Próximos a Vencer", "12", "⚠️", "red"),
                tarjeta_estadistica("Movimientos Hoy", "45", "🔄", "green"),
                columns="3",
                spacing="4",
                margin_y="2em",
            ),
        ),

        # 2. MÓDULO DE REGISTRO (Solo visible para Admin)
        formulario_registro(),

        # 3. TABLA DE INVENTARIO (Visible para todos, pero con lógica distinta)
        rx.vstack(
            rx.heading("Inventario General", size="4"),
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("ID"),
                        rx.table.column_header_cell("Descripción"),
                        rx.table.column_header_cell("Stock"),
                        rx.table.column_header_cell("Vencimiento"),
                    )
                ),
                rx.table.body(
                    rx.foreach(InventoryState.lista_insumos, render_fila_tabla)
                ),
                width="100%",
                variant="surface"
            ),
            
            # 4. BOTÓN DE SALIDA (Solo visible para Enfermera y Admin)
            rx.cond(
                (InventoryState.rol_usuario == "admin") | (InventoryState.rol_usuario == "enfermera"),
                rx.button("Registrar Salida de Insumo", color_scheme="orange", margin_top="1em")
            ),
            
            width="100%",
            margin_top="2em",
        ),
        max_width="1000px",
    )

def index() -> rx.Component:
    """Punto de entrada principal con lógica de autenticación."""
    return rx.box(
        rx.cond(
            InventoryState.esta_autenticado,
            dashboard_principal(), # Si está logueado, va al dashboard
            vista_login(),         # Si no, se queda en login
        )
    )

app = rx.App()
app.add_page(index, title="SySControl Hemodiálisis")