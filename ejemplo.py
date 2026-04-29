import reflex as rx
from .view.paciente_view import vista_paciente
from .view.insumo_view import vista_insumo
from .view.usuario_view import vista_usuario


app = rx.App()
app.add_page(vista_insumo, route="/")
