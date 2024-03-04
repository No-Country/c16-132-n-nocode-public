import reflex as rx
from esthetic_school.styles.colors import Color, TextColor
from esthetic_school.routes import Route

# from esthetic_school.styles.styles import Size, BUTTON_STYLE
from esthetic_school.components.common_button import common_button
from esthetic_school.components.heading import heading
from esthetic_school.styles.styles import Separation_size, Size
from esthetic_school.components.navbar import navbar
from esthetic_school.components.contact_form import contact_form


@rx.page( route="wellcome", title="Esthetic School - Bienvenida", image="simple_icon.png")
def wellcome() -> rx.Component:
    return rx.center(
        
        rx.vstack(
            navbar(),
            rx.vstack(
                heading(
                    "Bienvenidos a",
                    True
                ),
                rx.image(
                    src="/logo_grande.png",
                    alt="imagen del curso 1, de limpieza facial"
                ),
                rx.text(
                    "Desarrolla tu destreza en estética con nuestra app de cursos especializados.",
                    size=Size.MEDIUM.value
                ),
                common_button(
                    Route.COURSES.value,
                    "Ver los cursos",
                ),
                align="center",
                spacing=Size.MEDIUM.value,
                
            ),
            contact_form(),
            width="100%",
            height="100vh",
            align="center",
            justify="center",
            margin_y=Separation_size.SMALL.value
        ),
        margin_y=Separation_size.SMALL.value,
        width="100%",
    )
