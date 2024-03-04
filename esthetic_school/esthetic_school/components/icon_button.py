import reflex as rx

from esthetic_school.styles.colors import Color
from esthetic_school.styles import styles

def icon_button(icon: str, url: str, text="", solid=False) -> rx.Component:
    return rx.link(
        rx.chakra.button(
            rx.icon(icon),
            text,
            variant="solid" if solid else "ghost",
            margin_x="2em",
            style=styles.BUTTON_STYLE
            #bg=Color.PRIMARY.value,
            #color=Color.WHITE.value,
        ),
        href=url
    )