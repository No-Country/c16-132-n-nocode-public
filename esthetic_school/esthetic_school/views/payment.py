import reflex as rx

from esthetic_school.components.navbar import navbar
from esthetic_school.components.common_button import common_button
from esthetic_school.components.heading import heading
from esthetic_school.styles.styles import Size
from esthetic_school.routes import Route


@rx.page(route=Route.PAYMENT.value, title="Pagar")
def payment() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.vstack(
            rx.vstack(
                heading("Pagar"),
                rx.divider(),
                rx.input(
                    placeholder="Numero de tarjeta",
                    name="credit_number",
                    size="3",
                    type="number",
                ),
                rx.hstack(
                    rx.input(
                        placeholder="Nombre del titular",
                        name="card_owner_name",
                        size="3",
                    ),
                    rx.input(
                        placeholder="Apellido del titular",
                        name="card_owner_surname",
                        size="3",
                    ),
                ),
                rx.hstack(
                    rx.input(
                        placeholder="Codigo de seguridad",
                        name="security_code",
                        size="3",
                        type="password",
                    ),
                    rx.input(
                        placeholder="Fecha de vencimiento",
                        name="due_date",
                        size="3",
                        type="date",
                    ),
                ),
                common_button("url", "Enviar"),
                align="center",
            ),
            spacing=Size.BIG.value,
            # bg="violet",
            width="100%",
            height="100vh",
            align="center",
            justify="center",
        ),
        # inferior_bar(),
        width="100%",
        height="100vh",
        # spacing=Size.MEDIUM.value
        # bg="green"
    )
