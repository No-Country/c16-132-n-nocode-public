import reflex as rx

from esthetic_school.components.heading import heading
from esthetic_school.components.icon_button import icon_button
from esthetic_school.styles import styles



def course_card(
    img: str, heading_text: str, description: str, url: str) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.avatar(
                src=img,
                color="red",
                size="8"
            ),
            rx.heading(heading_text, as_="h4", size="4", align="center"),
            rx.text(description),
            icon_button("eye", url, "Ver más"),
            align="center",
            justify="center",
            spacing="4"
        ),
        style=styles.CARD_STYLE
    )
