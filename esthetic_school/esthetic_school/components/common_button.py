import reflex as rx

from esthetic_school.styles.colors import Color, TextColor
from esthetic_school.styles import styles

def common_button(url: str, text="", solid=False, color=False) -> rx.Component:
    return rx.link(
        rx.chakra.button(
            text,
            variant="solid" if solid else "ghost",
            style=styles.BUTTON_STYLE if color else styles.BUTTON_COLOR_STYLE
        ),
        href=url
    )