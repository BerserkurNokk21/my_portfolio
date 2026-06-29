from enum import Enum
import reflex as rx

MAX_WIDTH = "1100px"
IMAGE_HEIGHT = "200px"


class EmSize(Enum):
    DEFAULT = "1em"
    MEDIUM = "2em"
    BIG = "4em"


class Size(Enum):
    ZERO = "0"
    SMALL = "2"
    DEFAULT = "4"
    MEDIUM = "6"
    BIG = "8"


STYLESHEETS = [
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css",
    "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;700&display=swap",
    "/styles.css",
]

BASE_STYLE = {
    "body": {
        "background_color": "black",
        "color": "white",
        "font_family": "'Inter', sans-serif",
        "overflow_x": "hidden"
    },
    rx.button: {
        "--cursor-button": "pointer"
    }
}
