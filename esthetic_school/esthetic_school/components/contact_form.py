import reflex as rx

from esthetic_school.components.heading import heading
from esthetic_school.components.icon_button import icon_button

def contact_form() -> rx.Component:
    return rx.center(
        rx.vstack(
            heading(
                "¿Querés saber más? ¡Contactanos!",
            ),
            rx.divider(),
            rx.hstack(
                rx.chakra.input(
                    placeholder="Nombre",
                    is_required=True,
                    size="md"
                ),
                rx.chakra.input(
                    placeholder="Email@mail.com",
                    is_required=True,
                    size="md"
                ),
            ),
            rx.chakra.text_area(
                variant="outline", 
                placeholder="Ingrese su consulta", 
                is_required=True
            ),
            icon_button(
                "mail",
                "url",
                "Enviar"
            ),
            align="center",
            margin_y="4em"
        )
    )
