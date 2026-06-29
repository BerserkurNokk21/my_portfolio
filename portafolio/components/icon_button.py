import reflex as rx


def icon_button(icon: str, url: str, text="", solid=False) -> rx.Component:
    return rx.link(
        rx.button(
            rx.icon(icon),
            text,
            variant="solid" if solid else "surface",
            size="2",
            color="#a0a0a0" if not solid else "white",
            _hover={
                "color": "white",
                "background": "rgba(255, 255, 255, 0.1)"
            }
        ),
        href=url,
        is_external=True
    )
