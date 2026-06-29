import reflex as rx
from portafolio.components.heading import heading
from portafolio.data import Technology
from portafolio.styles.styles import EmSize, Size


def tech_stack(technologies: list[Technology]) -> rx.Component:
    return rx.vstack(
        heading("Tecnologias"),
        rx.flex(
            *[
                rx.badge(
                    rx.box(
                        class_name=technology.icon,
                        font_size="20px"
                    ),
                    rx.text(technology.name, font_size="0.85em"),
                    size="2",
                    color_scheme="gray",
                    variant="soft",
                    padding_x="0.8em",
                    padding_y="0.5em"
                )
                for technology in technologies
            ],
            wrap="wrap",
            spacing=Size.SMALL.value
        ),
        spacing=Size.DEFAULT.value,
        padding_y="1em"
    )
