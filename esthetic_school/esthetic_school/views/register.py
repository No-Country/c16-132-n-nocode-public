import reflex as rx

from esthetic_school.components.green_button import green_button
from esthetic_school.routes import Route
from esthetic_school.styles.styles import Size
from esthetic_school.components.navbar import navbar
#from esthetic_school.components.inferior_bar import inferior_bar
from esthetic_school.styles.colors import Color
from esthetic_school.components.heading import heading


@rx.page(route=Route.REGISTER_ROUTE.value, title="Registro")
def register() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.vstack(
            rx.vstack(
                heading(
                    "Registrarse"
                ),
                rx.divider(),
                rx.input(
                    placeholder="Nombre/s",
                    name="nombre",
                    size="3"
                ),
                rx.input(
                    placeholder="Apellido/s",
                    name="apellido",
                    size="3"
                ),
                rx.input(
                    placeholder="email@email.com",
                    name="email",
                    size="3",
                    type="email"
                ),
                rx.input(
                    placeholder="Contraseña",
                    name="contrasña",
                    size="3",
                    type="password"
                ),
                rx.input(
                    placeholder="Confirmar contraseña",
                    name="confirmar_contraseña",
                    size="3",
                    type="password"
                ),
                green_button(
                    "url",
                    "Registrarse"
                ),
                align="center"
            ),
            spacing=Size.BIG.value,
            #bg="violet",
            width="100%",
            height="100vh",
            align="center",
            justify="center"
        ),
        #inferior_bar(),
        width="100%",
        height="100vh",
        #spacing=Size.MEDIUM.value
        #bg="green"
    )