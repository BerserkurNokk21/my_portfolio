import reflex as rx
from portafolio import data
from portafolio.styles.styles import BASE_STYLE, MAX_WIDTH, STYLESHEETS, EmSize, Size
from portafolio.views.about import about
from portafolio.views.extra import extra
from portafolio.views.footer import footer
from portafolio.views.hero import hero
from portafolio.views.info import info
from portafolio.views.tech_stack import tech_stack
from portafolio.components.navbar import navbar
from portafolio.components.scroll_indicator import scroll_indicator

DATA = data.data


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            navbar(),
            hero(DATA),
            scroll_indicator(),
            rx.divider(border_color="rgba(255, 255, 255, 0.05)"),
            about(DATA.about),
            rx.divider(border_color="rgba(255, 255, 255, 0.05)"),
            tech_stack(DATA.technologies),
            rx.divider(border_color="rgba(255, 255, 255, 0.05)"),
            info("Experiencia", DATA.experience),
            info("Proyectos", DATA.projects),
            info("Formacion", DATA.training),
            extra(DATA.extras),
            rx.divider(border_color="rgba(255, 255, 255, 0.05)"),
            footer(DATA.media),
            spacing=Size.MEDIUM.value,
            padding_x=EmSize.MEDIUM.value,
            padding_y=EmSize.BIG.value,
            max_width=MAX_WIDTH,
            width="100%",
            class_name="grid-bg"
        ),
        width="100%"
    )


app = rx.App(
    stylesheets=STYLESHEETS,
    style=BASE_STYLE,
    theme=rx.theme(
        appearance="dark",
        accent_color="purple",
        grayColor="slate",
        radius="full"
    )
)

title = DATA.title
description = DATA.description
image = DATA.image

app.add_page(
    index,
    title=title,
    description=description,
    image=image,
    meta=[
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": image}
    ]
)
