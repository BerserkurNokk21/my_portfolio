import reflex as rx
from portafolio.components.heading import heading


def about(description: str) -> rx.Component:
    return rx.vstack(
        heading("Sobre mi"),
        rx.text(
            description,
            color="#a0a0a0",
            line_height="1.8"
        ),
        spacing="4",
        id="about",
        padding_y="1em"
    )
