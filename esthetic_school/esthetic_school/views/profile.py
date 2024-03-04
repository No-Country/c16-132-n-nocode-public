import reflex as rx

from esthetic_school.components.heading import heading
from esthetic_school.components.common_button import common_button
from esthetic_school.components.navbar import navbar
from esthetic_school.routes import Route

@rx.page(
        route=Route.PROFILE.value,
        title="Perfil"
)

def profile() -> rx.Component:
    return rx.center(
        navbar(),
        rx.vstack(
            rx.vstack(
                rx.chakra.avatar(color_scheme="pink", size="xl"),
                heading("Nombre", True),
                heading("mail@mail.com"),
                align="center"
            ),
            rx.divider(width="25%"),
            rx.hstack(
                common_button(
                    Route.LOGIN_ROUTE.value,
                    "Iniciar Sesion",
                    True,
                    True
                ),
                common_button(
                    Route.REGISTER_ROUTE.value, 
                    "Registrarse"
                ),
            ),
            # bg='pink',
            width="50%",
            height="50vh",
            align="center",
            justify="center",
        ),
        align="center",
        width="100%",
        height="100vh",
    )
