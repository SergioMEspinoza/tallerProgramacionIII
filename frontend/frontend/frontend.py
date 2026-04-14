# Importamos la librería Reflex y la llamamos 'rx' para escribir menos
import reflex as rx

# Esta clase 'State' es el cerebro de tu aplicación. 
# Aquí se guardarán los datos cuando conectemos el backend.
class State(rx.State):
    pass

# Función para crear una "Tarjeta de Estadística" (Stock, Vencimientos, etc.)
def tarjeta_estadistica(titulo, valor, icono, color):
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
        text_align="center",
        background="white",
    )

# Función principal que construye lo que el ojo humano verá
def index() -> rx.Component:
    return rx.container(
        # 1. ENCABEZADO Y NAVEGACIÓN
        rx.heading("Sistema de Control de Insumos - Centro de Hemodiálisis", size="8", margin_bottom="1em"),
        
        rx.hstack(
            rx.button("Insumos", color_scheme="blue"),
            rx.button("Inventario", color_scheme="green"),
            rx.button("Entradas", color_scheme="orange"),
            rx.button("Salidas", color_scheme="red"),
            rx.button("Reportes", color_scheme="purple"),
            spacing="4",
            margin_bottom="2em",
        ),

        # 2. SECCIÓN DE ESTADÍSTICAS (Dashboard rápido)
        rx.grid(
            tarjeta_estadistica("Stock Actual", "1,240 unidades", "📦", "blue"),
            tarjeta_estadistica("Próximos a Vencer", "12 items", "⚠️", "red"),
            tarjeta_estadistica("Movimientos Hoy", "45", "🔄", "green"),
            columns="3",
            spacing="4",
            width="100%",
            margin_bottom="2em",
        ),

        # 3. FORMULARIO DE INGRESO (Para que el usuario escriba)
        rx.card(
            rx.vstack(
                rx.heading("Registro de Nuevo Insumo", size="4"),
                rx.input(placeholder="Nombre del Insumo (ej. Filtro Dializador)", width="100%"),
                rx.hstack(
                    rx.input(placeholder="Cantidad inicial", type="number", width="50%"),
                    rx.input(placeholder="Fecha de Vencimiento", type="date", width="50%"),
                    width="100%",
                ),
                rx.button("Guardar en Base de Datos (Simulado)", width="100%", color_scheme="blue"),
                spacing="3",
            ),
            padding="2em",
            margin_bottom="2em",
        ),

        # 4. TABLA DE DATOS (Donde se verían los resultados)
        rx.vstack(
            rx.heading("Lista de Insumos en Almacén", size="4"),
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("ID"),
                        rx.table.column_header_cell("Nombre"),
                        rx.table.column_header_cell("Stock"),
                        rx.table.column_header_cell("Vencimiento"),
                    ),
                ),
                rx.table.body(
                    # Estas filas son "estáticas" (falsas) solo para ver el diseño
                    rx.table.row(
                        rx.table.cell("1"),
                        rx.table.cell("Solución Bicarbonato"),
                        rx.table.cell("500"),
                        rx.table.cell("2026-12-01"),
                    ),
                    rx.table.row(
                        rx.table.cell("2"),
                        rx.table.cell("Agujas Fistulares"),
                        rx.table.cell("2000"),
                        rx.table.cell("2027-05-15"),
                    ),
                ),
                width="100%",
            ),
            width="100%",
        ),
        padding="2em",
    )

# Configuramos la aplicación
app = rx.App()
# Decimos que la página principal ('/') cargue la función 'index'
app.add_page(index)
