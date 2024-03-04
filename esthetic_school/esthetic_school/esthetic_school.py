from rxconfig import config
import reflex as rx

from esthetic_school.views.wellcome import wellcome
from esthetic_school.views.courses import courses
from esthetic_school.views.profile import profile
from esthetic_school.views.pruebas import pruebas


def index() -> rx.Component:
    return rx.center(
        pruebas()
    )

app = rx.App()
app.add_page(index)

