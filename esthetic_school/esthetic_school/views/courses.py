import reflex as rx
from esthetic_school.routes import Route
from esthetic_school.components.navbar import navbar
from esthetic_school.components.heading import heading
from esthetic_school.styles.styles import Color
from esthetic_school.states.states import show_information


@rx.page(
    route=Route.COURSES.value, title="Esthetic School - Cursos", image="logo_mini.svg"
)
def courses() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.vstack(
                navbar(),
                heading("Nuestros Cursos", True),
                width="100%",
                align="center",
                #margin_y="2em"
            ),
            rx.divider(bg=Color.TERTIARY.value),
            rx.vstack(show_information()),
            width="60%"
        ),
        width="100%",
        margin_y="6em"
    )
