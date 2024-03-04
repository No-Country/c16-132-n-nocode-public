import reflex as rx
from esthetic_school.components.icon_button import icon_button

from esthetic_school.routes import Route

def inferior_bar() -> rx.Component:
    return rx.vstack(
        rx.flex(
            icon_button(
                #Profile
                "circle-user",
                Route.REGISTER,
                "Perfil",
                True,
            ),
            icon_button(
                #Courses
                "graduation-cap",
                "/courses",
                "Cursos",
                True
            ),
            icon_button(
                #Info
                "info",
                "url",
                "Info",
                True
            ),
            icon_button(
                #Back
                "arrow-left",
                "url",
                "Volver",
                True,
            ),
            bg="red",
            width="100%",
            height="4em",
            justify="between",
            align="center",
            bottom="0px",
            spacing="8",
            position="fixed"
        ),
        width="100%"
    )