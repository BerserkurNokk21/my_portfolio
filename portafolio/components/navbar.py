import reflex as rx
from portafolio.styles.styles import Size, EmSize


def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.link(
                rx.text(
                    "oscar.dev",
                    font_weight="bold",
                    font_size="1.1em",
                    color="white"
                ),
                href="#",
            ),
            rx.hstack(
                rx.link(
                    "Home",
                    href="#home",
                    color="#a0a0a0",
                    _hover={"color": "white"},
                    font_size="0.9em"
                ),
                rx.link(
                    "Sobre mí",
                    href="#about",
                    color="#a0a0a0",
                    _hover={"color": "white"},
                    font_size="0.9em"
                ),
                rx.link(
                    "Proyectos",
                    href="#projects",
                    color="#a0a0a0",
                    _hover={"color": "white"},
                    font_size="0.9em"
                ),
                rx.link(
                    "Contacto",
                    href="#contact",
                    color="#a0a0a0",
                    _hover={"color": "white"},
                    font_size="0.9em"
                ),
                spacing="6",
                align="center"
            ),
            justify="between",
            width="100%",
            padding_x=EmSize.BIG.value,
            padding_y="0.8em",
            align="center"
        ),
        position="sticky",
        top="0",
        z_index="100",
        background="rgba(0, 0, 0, 0.8)",
        backdrop_filter="blur(10px)",
        border_bottom="1px solid rgba(255, 255, 255, 0.05)",
        width="100%"
    )
