import reflex as rx
from typing import List, Optional
from pydantic import BaseModel

class InsumoSchema(BaseModel):
    id: int
    nombre: str
    cantidad: int
    vencimiento: str

class InventoryState(rx.State):
    # --- ESTADO DE USUARIO ---
    usuario_logueado: str = ""
    password_input: str = ""
    rol_usuario: str = ""  # "admin", "enfermera", "medico"
    esta_autenticado: bool = False

    # --- DATOS DE INVENTARIO ---
    lista_insumos: List[InsumoSchema] = [
        InsumoSchema(id=1, nombre="Filtro Dializador", cantidad=50, vencimiento="2026-05-20"),
    ]
    nuevo_nombre: str = ""
    nueva_cantidad: str = ""
    nueva_fecha: str = ""
    
    # --- SETTERS ---
    # Estos métodos permiten que los componentes de la vista actualicen el estado
    def set_usuario_logueado(self, valor: str): self.usuario_logueado = valor
    def set_password_input(self, valor: str): self.password_input = valor
    def set_nuevo_nombre(self, valor: str): self.nuevo_nombre = valor
    def set_nueva_cantidad(self, valor: str): self.nueva_cantidad = valor
    def set_nueva_fecha(self, valor: str): self.nueva_fecha = valor

    def login(self):
        """Simulación de autenticación por roles."""
        users = {
            "admin": ("admin123", "admin"),
            "enfermera": ("enfer123", "enfermera"),
            "medico": ("med123", "medico")
        }
        
        if self.usuario_logueado in users and users[self.usuario_logueado][0] == self.password_input:
            self.rol_usuario = users[self.usuario_logueado][1]
            self.esta_autenticado = True
        else:
            return rx.window_alert("Credenciales incorrectas")

    def logout(self):
        self.esta_autenticado = False
        self.usuario_logueado = ""
        self.password_input = ""

    def agregar_insumo_local(self):
        # Solo admin puede agregar
        if self.rol_usuario != "admin":
            return rx.window_alert("No tiene permisos para esta acción")
        
        nuevo = InsumoSchema(
            id=len(self.lista_insumos) + 1,
            nombre=self.nuevo_nombre,
            cantidad=int(self.nueva_cantidad) if self.nueva_cantidad else 0,
            vencimiento=self.nueva_fecha
        )
        self.lista_insumos.append(nuevo)
        self.nuevo_nombre = ""
        self.nueva_cantidad = ""
        self.nueva_fecha = ""