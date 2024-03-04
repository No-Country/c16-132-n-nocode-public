import reflex as rx

rx.popover.root(
    rx.popover.trigger(
        rx.button("Popover"),
    ),
    rx.popover.content(
        rx.flex(
            rx.text("Simple Example"),
            rx.popover.close(
                rx.button("Close"),
            ),
            direction="column",
            spacing="3",
        ),
    ),
)