import reflex as rx

from esthetic_school.styles.colors import Color, TextColor
from esthetic_school.styles import styles

class RedButtonState(rx.State):
    def show(self) -> rx.Component:
        print("Operación Cancelada")
        return rx.window_alert("Operación cancelada")

def red_button(url: str, text="", solid=False) -> rx.Component:
    return rx.link(
        rx.chakra.button(
            text,
            variant="solid" if solid else "ghost",
            style=styles.RED_BUTTON,
            on_click=RedButtonState.show,
        ),
        href="#",
    )