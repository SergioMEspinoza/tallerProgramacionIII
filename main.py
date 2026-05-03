import reflex as rx
from .view.paciente_view import vista_paciente
from .view.insumo_view import vista_insumo
from .view.usuario_view import vista_usuario
from .view.entrada_view import vista_entrada
from .view.salida_view import vista_salida


app = rx.App()
app.add_page(vista_salida, route="/")
