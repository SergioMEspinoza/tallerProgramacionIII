import reflex as rx

config = rx.Config(
    app_name="proyecto_taller",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)