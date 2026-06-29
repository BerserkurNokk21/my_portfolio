import reflex as rx
from portafolio.data import Extra

from portafolio.styles.styles import IMAGE_HEIGHT, Size


def card_detail(extra: Extra) -> rx.Component:
    return rx.card(
        rx.link(
            rx.inset(
                rx.image(
                    src=extra.image,
                    height=IMAGE_HEIGHT,
                    width="100%",
                    object_fit="cover",
                    border_radius="8px"
                ),
                pb=Size.DEFAULT.value
            ),
            rx.text.strong(extra.title, color="white"),
            rx.text(
                extra.description,
                size=Size.SMALL.value,
                color="#888",
                line_height="1.5"
            )
        ),
        width="100%",
        href=extra.url,
        is_external=True,
        background="rgba(255, 255, 255, 0.02)",
        border="1px solid rgba(255, 255, 255, 0.05)",
        border_radius="16px",
        padding="0.8em",
        _hover={
            "background": "rgba(255, 255, 255, 0.04)",
            "border_color": "rgba(255, 255, 255, 0.1)",
            "transform": "translateY(-2px)"
        },
        transition="all 0.3s ease"
    )
