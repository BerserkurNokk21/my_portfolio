import reflex as rx
from portafolio.components.heading import heading
from portafolio.data import Data
from portafolio.styles.styles import Size, EmSize


def hero(data: Data) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.flex(
                rx.vstack(
                    rx.text(
                        "• AVAILABLE FOR WORK",
                        color="#4ade80",
                        font_size="0.8em",
                        font_weight="bold",
                        letter_spacing="0.15em",
                        margin_bottom="0.5em"
                    ),
                    rx.heading(
                        "Oscar Peris Espejo",
                        font_size="4em",
                        font_weight="900",
                        line_height="1.1",
                        letter_spacing="-0.02em"
                    ),
                    rx.text(
                        data.skill,
                        font_size="1.2em",
                        color="#c0c0c0",
                        margin_top="0.3em"
                    ),
                    rx.text(
                        data.about[:120] + "...",
                        font_size="0.9em",
                        color="#808080",
                        max_width="400px",
                        line_height="1.6",
                        margin_top="0.5em"
                    ),
                    rx.flex(
                        rx.badge("Unity", color_scheme="gray", variant="soft", size="2"),
                        rx.badge("C#", color_scheme="gray", variant="soft", size="2"),
                        rx.badge("Python", color_scheme="gray", variant="soft", size="2"),
                        rx.badge("PostgreSQL", color_scheme="gray", variant="soft", size="2"),
                        spacing="3",
                        wrap="wrap",
                        margin_top="1em"
                    ),
                    rx.flex(
                        rx.link(
                            rx.button(
                                rx.icon("arrow-down"),
                                "Explore my work below",
                                variant="surface",
                                size="2"
                            ),
                            href="#about"
                        ),
                        rx.text(
                            "• Open to full-time & freelance opportunities",
                            font_size="0.8em",
                            color="#606060",
                            margin_top="0.5em"
                        ),
                        flex_direction="column",
                        margin_top="1.5em"
                    ),
                    spacing="2",
                    align="start",
                    width="100%"
                ),
                rx.box(
                    lanyard_photo(data.avatar),
                    position="relative",
                    display=["none", "none", "block"]
                ),
                justify="between",
                width="100%",
                align="center"
            ),
            spacing="8",
            width="100%"
        ),
        id="home",
        padding_y=EmSize.BIG.value,
        padding_x=EmSize.MEDIUM.value,
        width="100%"
    )


def lanyard_photo(avatar: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(
                "ID CARD",
                position="absolute",
                top="-2em",
                right="-0.5em",
                font_size="0.7em",
                font_weight="bold",
                letter_spacing="0.2em",
                color="#555",
                writing_mode="vertical-rl",
                text_orientation="mixed"
            ),
            rx.image(
                src=avatar,
                width="280px",
                height="350px",
                object_fit="cover",
                border_radius="12px",
                filter="grayscale(100%) contrast(1.1) brightness(0.9)",
                border="3px solid rgba(255,255,255,0.1)"
            ),
            position="relative",
            padding="10px",
            background="rgba(20, 20, 20, 0.8)",
            border_radius="16px",
            box_shadow="0 20px 60px rgba(0,0,0,0.5), 0 0 40px rgba(100,100,255,0.05)",
            transform="perspective(1000px) rotateY(-5deg) rotateX(2deg)",
            transition="transform 0.5s ease",
            _hover={
                "transform": "perspective(1000px) rotateY(0deg) rotateX(0deg)"
            }
        ),
        position="relative",
        margin_top="2em"
    )
