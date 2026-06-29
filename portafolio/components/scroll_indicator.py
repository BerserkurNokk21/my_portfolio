import reflex as rx
from portafolio.styles.styles import Size


def scroll_indicator() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.text(
                "SCROLL",
                font_size="0.7em",
                letter_spacing="0.3em",
                color="#555",
                font_weight="bold"
            ),
            rx.box(
                width="1px",
                height="40px",
                background="linear-gradient(to bottom, #555, transparent)",
                animation="scrollPulse 2s ease-in-out infinite"
            ),
            spacing="2",
            align="center"
        ),
        padding_top="2em",
        padding_bottom="1em"
    )
