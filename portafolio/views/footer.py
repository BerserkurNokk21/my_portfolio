import reflex as rx
from portafolio.components.media import media
from portafolio.data import Media
from portafolio.styles.styles import Size


def footer(data: Media) -> rx.Component:
    return rx.vstack(
        rx.text(
            "Oscar Peris Espejo",
            font_size="0.9em",
            color="#555"
        ),
        media(data),
        rx.text(
            "Designed & Built with Reflex",
            font_size="0.7em",
            color="#333",
            margin_top="1em"
        ),
        spacing=Size.SMALL.value,
        align="center",
        padding_y="2em"
    )
