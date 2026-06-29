import reflex as rx
from portafolio.components.icon_badge import icon_badge
from portafolio.components.icon_button import icon_button
from portafolio.data import Info
from portafolio.styles.styles import IMAGE_HEIGHT, EmSize, Size


def info_detail(info: Info) -> rx.Component:
    return rx.flex(
        rx.hstack(
            icon_badge(info.icon),
            rx.vstack(
                rx.text.strong(info.title, color="white"),
                rx.text(info.subtitle, color="#888", font_size="0.9em"),
                rx.text(
                    info.description,
                    size=Size.SMALL.value,
                    color="#666",
                    white_space="pre-line",
                    line_height="1.6"
                ),
                rx.cond(
                    info.technologies,
                    rx.flex(
                        *[
                            rx.badge(
                                rx.box(class_name=technology.icon),
                                technology.name,
                                color_scheme="gray",
                                variant="soft"
                            )
                            for technology in info.technologies
                        ],
                        wrap="wrap",
                        spacing=Size.SMALL.value
                    )
                ),
                rx.hstack(
                    rx.cond(
                        info.url != "",
                        icon_button(
                            "link",
                            info.url
                        )
                    ),
                    rx.cond(
                        info.github != "",
                        icon_button(
                            "github",
                            info.github
                        )
                    ),
                    rx.cond(
                        info.tdd != "",
                        icon_button(
                            "file-text",
                            info.tdd
                        )
                    ),
                    rx.cond(
                        info.gitlab != "",
                        icon_button(
                            "gitlab",
                            info.tdd
                        )
                    )
                ),
                spacing=Size.SMALL.value,
                width="100%"
            ),
            spacing=Size.DEFAULT.value,
            width="100%"
        ),
        rx.cond(
            info.image != "",
            rx.image(
                src=info.image,
                height=IMAGE_HEIGHT,
                width="auto",
                border_radius=EmSize.DEFAULT.value,
                object_fit="cover"
            )
        ),
        rx.vstack(
            rx.cond(
                info.date != "",
                rx.badge(info.date, color_scheme="gray", variant="soft")
            ),
            rx.cond(
                info.certificate != "",
                icon_button(
                    "shield-check",
                    info.certificate,
                    solid=True
                )
            ),
            spacing=Size.SMALL.value,
            align="end"
        ),
        flex_direction=["column-reverse", "row"],
        spacing=Size.DEFAULT.value,
        width="100%",
        padding="1em",
        border_radius="16px",
        background="rgba(255, 255, 255, 0.02)",
        border="1px solid rgba(255, 255, 255, 0.05)",
        _hover={
            "background": "rgba(255, 255, 255, 0.04)",
            "border_color": "rgba(255, 255, 255, 0.1)"
        },
        transition="all 0.3s ease"
    )
