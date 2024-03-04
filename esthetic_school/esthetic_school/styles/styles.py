import reflex as rx
from enum import Enum
from .colors import Color, TextColor

MAX_WIDTH = "990px"
FLEX_DIRECTION = ["column", "column", "column", "row", "row"]


class Size(Enum):
    ZERO = "0"
    SMALL = "2"
    MEDIUM = "4"
    DEFAULT = "6"
    BIG = "8"
    BUTTON = "9"

class Separation_size(Enum):
    ZERO = "0"
    SMALL = "2em"
    MEDIUM = "4em"
    BUTTON = "3em"
    BIG = "6em"


BASE_STYLE = {
    "color": TextColor.BLACK.value,
    "background": Color.PRIMARY.value,
}

HEADING_STYLE = {
    "color": TextColor.ACCENT.value,
    "font_size": "3em"
}

LINK_STYLE =  {
    "text_decoration": "none",
    "_hover": {
        "color": TextColor.ACCENT.value,
        "text_decoration": "none"
    }
}

BUTTON_STYLE = {
    "background": Color.PRIMARY.value,
    #"margin_bottom": Size.DEFAULT.value,
    "height": Separation_size.BUTTON.value,
    "color": f"{TextColor.WHITE.value} !important",
    "cursor":"pointer",
    "_hover": {
        "background": Color.SECONDARY.value,
        "box-shadow": "rgb(38, 57, 77) 0px 20px 30px -10px",
        "transition": "ease .5s"
    }
}

BUTTON_COLOR_STYLE = {
    "background": Color.TERTIARY.value,
    #"margin_bottom": Size.DEFAULT.value,
    "height": Separation_size.BUTTON.value,
    "color": f"{TextColor.WHITE.value} !important",
    "cursor":"pointer",
    "_hover": {
        "box-shadow": "rgb(38, 57, 77) 0px 20px 30px -10px",
        "transition": "ease .5s"
    }
}

GREEN_BUTTON = {
    "background": Color.SECONDARY.value,
    #"margin_bottom": Size.DEFAULT.value,
    "height": Separation_size.BUTTON.value,
    "color": f"{TextColor.WHITE.value} !important",
    "cursor":"pointer",
    "_hover": {
        "box-shadow": "rgb(38, 57, 77) 0px 20px 30px -10px",
        "transition": "ease .5s"
    }
}



CARD_STYLE = {
    "_hover":{
        "box_shadow": "rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px",
        "transition": "ease .5s"
    }
}

max_width_style = dict(
    align_items="start",
    padding_x=Size.BIG.value,
    width="100%",
    max_width=MAX_WIDTH
)