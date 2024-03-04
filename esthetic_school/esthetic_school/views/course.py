import reflex as rx
import json

from esthetic_school.components.heading import heading
from esthetic_school.components.common_button import common_button
from esthetic_school.components.navbar import navbar
from esthetic_school.routes import Route
from esthetic_school.states.states import course_information


@rx.page(route=Route.COURSE_ROUTE.value)

def course() -> rx.Component:
    #course_id = CourseState.show_curse
    #course_data = get_course_data(course_id)
    #print(course_id)    
    return rx.center(
        navbar(),
        rx.vstack(
            rx.avatar(size="9"),
            heading("Nombre del curso", True),
            rx.text("Precio: $15000"),
            common_button(Route.PAYMENT.value, "Ir a pagar"),
            align="center",
            justify="center",
            margin_y="8em",
            #course_id = int(request.params["course_id"])
        )
    )

# ruta = '/home/franco/Desktop/c16-132-n-nocode/esthetic_school/esthetic_school/states/courses.json'
# def load_courses_file():
#     with open(ruta) as file:
#         return json.load(file)
    
# def get_course_data(course_id: int):
#     courses = load_courses_file()
#     return next((course for course in courses if f"{CourseState.show_curse == course["id"]}"), None)
